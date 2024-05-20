from django.contrib import admin
from products.models import ProductModel, ProductImg, ProductCategory, Order, Address
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

admin.site.register(ProductCategory)
admin.site.register(Order)
admin.site.register(Address)



class ProductImageAdmin(admin.StackedInline):
    model = ProductImg
 
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_price", "product_description", "user")
    list_filter = ("user", )
    inlines = [ProductImageAdmin]
    exclude = ('slug',)
 
    class Meta:
        model = ProductModel
 
@admin.register(ProductImg)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "by_user", "view_product_link")
    list_filter = ("product",)


    def by_user(self, obj):
        return obj.product.user

    def view_product_link(self, obj):
        url = (
            reverse("admin:products_productmodel_changelist") + f"{obj.product_id}"
        )
        return format_html(f'<a href="{url}"> ID-{obj.product_id}</a>')

    view_product_link.short_description = "Product ID"
