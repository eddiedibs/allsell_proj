import re
from django.contrib import admin
from allsellapp.models import HomeBanner, BannerImgs
from products.models import ProductModel, ProductImg, ProductCategory, Order, Address

# admin.site.register(ProductModel)
# admin.site.register(ProductImg)
admin.site.register(ProductCategory)
admin.site.register(Order)
admin.site.register(Address)




class BannerImageAdmin(admin.StackedInline):
    model = BannerImgs

class ProductImageAdmin(admin.StackedInline):
    model = ProductImg
 
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    exclude = ('slug',)
 
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