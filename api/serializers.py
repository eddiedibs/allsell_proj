from rest_framework import serializers
from products.models import ProductModel, OrderProduct, Order




class ListProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ("product_name","product_description","currency","product_price","user")

class ListOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("customer", "get_cart_amount_of_items", "get_cart_total")

class ListOrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = ("product","quantity","order", "total_amount", "total_amount_without_discount")
