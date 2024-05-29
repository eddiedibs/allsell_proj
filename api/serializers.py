from rest_framework import serializers
from products.models import ProductModel, OrderProduct, Order




class ListProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ("product_name","product_description","product_price","user")

class ListOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "customer", "get_cart_amount_of_items", "get_cart_total", "get_cart_total_as_float")

class ListOrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = ("product","quantity","order", "total_amount", "total_amount_without_discount", "is_amount_in_stock", "amount_in_stock")
