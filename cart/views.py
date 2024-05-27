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

from products.models import ProductModel, Order, OrderProduct
from allsellapp.models import HomeBanner
from cart.forms import AddressForm


class CartContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, ordered=False)
            items = order.orderproduct_set.all()
            context["items"] = items
            context["order"] = order
        else:
            context["items"] = []
            context["order"] = {"get_cart_total": 0, "get_cart_amount_of_items": 0}
        return context


class CartTemplateView(CartContextMixin, TemplateView):
    template_name = 'cart.html'


@method_decorator(csrf_protect, name='dispatch')
@method_decorator(sensitive_post_parameters(), name='dispatch')
@method_decorator(never_cache, name='dispatch')
class CheckoutTemplateView(CartContextMixin, TemplateView):
    template_name = 'checkout.html'


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Please sign-in to add items to checkout')
            return redirect(reverse_lazy('login_view'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        initial_data = {
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
                form = AddressForm(initial=initial_data)
                context["form"] = form
                return context

            else:
                messages.error(request, 'There was an error with your request.')
                return redirect(reverse_lazy('checkout_view'))
            
        else:
            return AddressForm()