from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from products.models import ProductModel, Order
from allsellapp.models import HomeBanner





class CartTemplateView(TemplateView):
    template_name = 'cart.html'

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

        return context

