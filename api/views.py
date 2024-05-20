from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from products.models import ProductModel
from users_allsell.models import User
from .serializers import ListProductSerializer



class ProductsListView(generics.ListAPIView):
    allowed_methods = ['GET']
    queryset = ProductModel.objects.all()
    serializer_class = ListProductSerializer


class ProductsCreateView(APIView):
    serializer_class = ListProductSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()


        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product_name = serializer.data.get("product_name")
            product_description = serializer.data.get("product_description")
            currency = serializer.data.get("currency")
            product_price = serializer.data.get("product_price")
            user = serializer.data.get("user")
            retrieved_user = User.objects.filter(id=user).first()
        

            product = ProductModel(product_name=product_name, 
                                product_description=product_description,
                                currency=currency,
                                product_price=product_price,
                                user=retrieved_user,
                                )
            product.save()

            return Response(ListProductSerializer(product).data, status=status.HTTP_201_CREATED)
        else:
            return Response({'Bad Request': 'Something went wrong...'}, status=status.HTTP_400_BAD_REQUEST)


class ProductsDestroyView(generics.DestroyAPIView):
    allowed_methods = ['DELETE']

    queryset = ProductModel.objects.all()
    serializer_class = ListProductSerializer
    
class ProductsUpdateView(generics.UpdateAPIView):
    allowed_methods = ['PUT']

    queryset = ProductModel.objects.all()
    serializer_class = ListProductSerializer