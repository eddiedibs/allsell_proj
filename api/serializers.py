from rest_framework import serializers
from products.models import ProductModel




class ListProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ("prod_name","prod_desc","currency","prod_price","user")