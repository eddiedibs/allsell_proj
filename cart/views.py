from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic import View as GenericView
from products.models import ProductModel, Order
from allsellapp.models import HomeBanner
from .utils import get_or_set_order_session




class CartTemplateView(TemplateView):
    template_name = "cart/cart.html"

    def get_context_data(self, **kwargs):
        context = super(CartTemplateView, self).get_context_data(**kwargs)
        context["order"] = get_or_set_order_session(self.request)
        return context


class IncreaseQuantityView(GenericView):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(Order, id=kwargs['pk'])
        order_item.quantity += 1
        order_item.save()
        return redirect("cart:cart_view")


class DecreaseQuantityView(GenericView):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(Order, id=kwargs['pk'])
        if order_item.quantity <= 1:
            order_item.delete()
        else:
            order_item.quantity -= 1
            order_item.save()
        return redirect("cart:cart_view")


class RemoveFromCartView(GenericView):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(Order, id=kwargs['pk'])
        order_item.delete()
        return redirect("cart:cart_view")

    # def get_context_data(self, **kwargs):

    #     products = self.model[0].objects.all()
    #     banners = self.model[1].objects.all().filter(banner_title='Clothing and Automobile Promo').first()

    #     all_data = {
    #         'products': products,
    #         'banners': banners,
    #     }

    #     return all_data


    # def get(self, request):
        
    #     return render(request, self.template_name, context=self.get_context_data())


# def home(request):
#     context = {
#         'products': ProductModel.objects.all(),
#         'banners': Home_banner.objects.all().filter(banner_title='Clothing and Automobile Promo').first(),
#     }


#     return render(request, 'allsellapp/home.html', context)

