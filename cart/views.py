import csv


from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.base import ContextMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from products.models import ProductModel, Order, OrderProduct
from allsellapp.models import HomeBanner
from cart.forms import AddressForm
from .utils import get_or_create_order



class CartContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            order = get_or_create_order(self, is_completed=False)
            items = order.orderproduct_set.all()
            context["items"] = items
            context["order"] = order
        else:
            context["items"] = []
            context["order"] = {"get_cart_total": 0, "get_cart_amount_of_items": 0}
        return context

@method_decorator(csrf_protect, name='dispatch')
@method_decorator(sensitive_post_parameters(), name='dispatch')
@method_decorator(never_cache, name='dispatch')
class BaseProtectedTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You need to be signed-in')
            return redirect(reverse_lazy('login_view'))
        return super().dispatch(request, *args, **kwargs)

class CartTemplateView(CartContextMixin, TemplateView):
    template_name = 'cart.html'



class PaymentTemplateView(BaseProtectedTemplateView, CartContextMixin, TemplateView):
    template_name = 'payment.html'


class CheckoutTemplateView(BaseProtectedTemplateView, CartContextMixin, TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        initial_data = {
            'user': self.request.user,
            'user_first_name': self.request.user.first_name,
            'user_last_name': self.request.user.last_name,
            # Include other fields you want to pre-populate here
        }
        context['forms'] = AddressForm(initial=initial_data)
        return context



    def post(self, request):
        if request.method == 'POST':
            form = AddressForm(request.POST)
            if form.is_valid():
                address = form.save()
                customer = self.request.user.customer
                order = get_or_create_order(self, is_completed=False)
                order.billing_address = address
                order.save()
                return redirect(reverse_lazy('payment_view'))
            else:
                messages.error(request, 'There was an error when sending the address, please try again.')
                return redirect(reverse_lazy('checkout_view'))
            
        else:
            return AddressForm()



class OrderDetailsTemplateView(BaseProtectedTemplateView, TemplateView):
    template_name = 'order_details.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = get_or_create_order(self, is_completed=True)
        items = order.orderproduct_set.all()
        context["items"] = items
        context["order"] = order
        return context

class OrdersCompletedTemplateView(BaseProtectedTemplateView, TemplateView):
    template_name = 'orders_completed.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            orders = Order.objects.filter(customer=customer).order_by('-start_date')
            context["orders"] = orders
        return context


class ExportOrdersCSVView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer).order_by('-start_date')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'

        writer = csv.writer(response)
        writer.writerow(['Order ID', 'Product(s)', 'Quantity', 'Price', 'Date Ordered'])

        for order in orders:
            writer.writerow([order.id, order.get_cart_items, order.get_cart_amount_of_items, order.get_cart_total, order.completed_date])

        return response

class ExportReceiptPDFView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        order = get_or_create_order(self, is_completed=True)
        items = order.orderproduct_set.all()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="receipt_{str(order.id)}.pdf"'

        # Create the PDF object, using the response object as its "file."
        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter

        # Add the centered image
        image_path = '/home/edd1e/scripts/projs/portfolio_stuff/allsell_proj/allsellapp/static/svgs/logo_bluebckgr.png'  # Update with your image path
        image = ImageReader(image_path)
        image_width, image_height = image.getSize()

        # Calculate the position to center the image
        x = (width - image_width) / 2
        y = (height - image_height) / 1

        p.drawImage(image, x, y, width=image_width, height=image_height)


        start_y = y - 40
        line_height = 20  # Adjust as needed for spacing between lines

        # Draw the text strings with even vertical spacing
        p.setFont("Helvetica", 12)
        p.drawString(100, start_y, f"Receipt for Order #{order.id}")
        p.drawString(100, start_y - line_height, f"Customer: {order.customer.user.username}")

        current_y = start_y - 2 * line_height
        for item in items:
            p.drawString(100, current_y, f"Product: {item.product.product_name}")
            current_y -= line_height
            p.drawString(100, current_y, f"Quantity: {item.quantity}")
            current_y -= line_height
            if item.product.product_discount:
                p.drawString(100, current_y, f"Price: {item.product.discount_price}")
            else:
                p.drawString(100, current_y, f"Price: {item.product.product_price}")
            current_y -= line_height  # Move to the next line for the next item

        larger_font_size = 18  # Adjust as needed for larger font size
        p.setFont("Helvetica-Bold", larger_font_size)
        p.drawString(100, current_y - 30, f"Total paid: {order.get_cart_total}")
        p.drawString(100, current_y - 50, f"Date Ordered: {order.completed_date.strftime('%Y-%m-%d %H:%M:%S')}")
        p.setFont("Helvetica", 12) 

        # Close the PDF object cleanly.
        p.showPage()
        p.save()

        return response

