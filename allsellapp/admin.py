import re
from django.contrib import admin
from allsellapp.models import HomeBanner, BannerImgs
from products.models import ProductModel, ProductImg, ProductCategory, Order

# admin.site.register(ProductModel)
# admin.site.register(ProductImg)
admin.site.register(ProductCategory)
admin.site.register(Order)

class BannerImageAdmin(admin.StackedInline):
    model = BannerImgs

class ProductImageAdmin(admin.StackedInline):
    model = ProductImg
 
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
 
    class Meta:
       model = ProductModel
 
@admin.register(ProductImg)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(HomeBanner)
class BannerAdmin(admin.ModelAdmin):
    inlines = [BannerImageAdmin]
    
    class Meta:
        model = HomeBanner