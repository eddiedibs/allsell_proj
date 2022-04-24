from django.shortcuts import render
from products.models import Product_model
from django.views.generic import DetailView, ListView
from django.views.generic.base import View

class ProdDetailView(DetailView):
    model = Product_model
    template_name = 'product.html'
    context_object_name = 'products'



