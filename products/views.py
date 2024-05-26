from django.shortcuts import render, get_object_or_404
from products.models import ProductModel
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.base import View

class ProdDetailView(DetailView):
    model = ProductModel
    template_name = 'product.html'
    context_object_name = 'products'


    def get_object(self):
        return get_object_or_404(ProductModel, slug=self.kwargs["slug"])




class ProdSellView(TemplateView):
    template_name = 'choosewhattosell.html'


