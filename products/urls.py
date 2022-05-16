from django.contrib import admin
from django.urls import path
from products import views as product_views

urlpatterns = [
    # path('', views.home, name='home_view'),
    path('product/<slug:slug>/', product_views.ProdDetailView.as_view(template_name='products/product.html'), name='product_view'),
    path('profile/sellitem/', product_views.ProdSellView.as_view(template_name='products/choosewhattosell.html'), name='sell_item_view'),
    path('product/<slug>/', product_views.ProdDetailView.as_view(template_name='products/product.html'), name='product_view'),


]
