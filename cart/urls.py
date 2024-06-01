from django.contrib import admin
from django.urls import path
from cart import views as cart_views

urlpatterns = [
    path('cart/', cart_views.CartTemplateView.as_view(template_name='cart/cart.html'), name='cart_view'),
    path('checkout/', cart_views.CheckoutTemplateView.as_view(template_name='cart/checkout.html'), name='checkout_view'),
    path('payment/', cart_views.PaymentTemplateView.as_view(template_name='cart/payment.html'), name='payment_view'),
    path('order-details/<pk>', cart_views.OrderDetailsTemplateView.as_view(template_name='cart/order_details.html'), name='order_details_view'),
    path('orders-completed/', cart_views.OrdersCompletedTemplateView.as_view(template_name='cart/orders_completed.html'), name='orders_completed_view'),
    path('export-orders/', cart_views.ExportOrdersCSVView.as_view(), name='export_orders_csv'),
    path('export-order-receipt/', cart_views.ExportReceiptPDFView.as_view(), name='export_order_receipt_pdf'),
]
