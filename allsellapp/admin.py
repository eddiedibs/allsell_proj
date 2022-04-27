import re
from django.contrib import admin
from products.models import Product_model, Product_imgs

admin.site.register(Product_model)
admin.site.register(Product_imgs)
