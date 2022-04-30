import re
from django.contrib import admin
from products.models import Product_model, Product_img, Product_category

# admin.site.register(Product_model)
# admin.site.register(Product_img)
# admin.site.register(Product_category)


class ProductImageAdmin(admin.StackedInline):
    model = Product_img
 
@admin.register(Product_model)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
 
    class Meta:
       model = Product_model
 
@admin.register(Product_img)
class ProductImageAdmin(admin.ModelAdmin):
    pass
