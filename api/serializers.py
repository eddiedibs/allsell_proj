from rest_framework import serializers
from products.models import ProductModel




class ListProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ("product_name","product_description","currency","product_price","user")