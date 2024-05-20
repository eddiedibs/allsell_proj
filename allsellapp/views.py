from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from products.models import ProductModel, Order, ProductImg
from allsellapp.models import HomeBanner




class HomeListView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.objects.all()
        context['banners'] = HomeBanner.objects.all().filter(banner_title='Clothing and Automobile Promo').first()

        return context




