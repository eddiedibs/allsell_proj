from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import DetailView, ListView, TemplateView
from products.models import ProductModel, Order, OrderProduct
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.base import ContextMixin
from allsellapp.models import HomeBanner



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



class CheckoutTemplateView(CartContextMixin, TemplateView):
    template_name = 'checkout.html'
