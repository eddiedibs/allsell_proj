from django.contrib import admin
from django.urls import path
from cart import views as cart_views

urlpatterns = [
    path('cart/', cart_views.CartTemplateView.as_view(template_name='cart/cart.html'), name='cart_view'),
]
