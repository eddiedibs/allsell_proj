from django.contrib import admin
from django.urls import path
from cart import views as cart_views

urlpatterns = [
    path('cart/', cart_views.CartTemplateView.as_view(template_name='cart/cart.html'), name='cart_view'),
    path('checkout/', cart_views.CheckoutTemplateView.as_view(template_name='cart/checkout.html'), name='checkout_view'),
    path('payment/', cart_views.PaymentTemplateView.as_view(template_name='cart/payment.html'), name='payment_view'),

]
