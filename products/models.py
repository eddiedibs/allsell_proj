import uuid

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image
from .categories_and_colortags import categories, color_tags
from django.utils.text import slugify




class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.zip_code}"

    class Meta:
        verbose_name_plural = 'Addresses'




class ProductCategory(models.Model):

    category = models.CharField(max_length=225, choices=categories, default='Category_test')
    color_tag = models.CharField(max_length=225, choices=color_tags, default='color_test')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.category

    # def get_absolute_url(self):
    #     return reverse('category_detail', kwargs={'slug': self.slug})



class ProductModel(models.Model):
    currencies = [
    ('$', "US Dollars ($)"), 
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    slug = models.SlugField(unique=True, blank=True, default=None)
    product_name = models.CharField(max_length=40)
    product_description = models.TextField(max_length=500)
    currency = models.CharField(max_length=5, choices=currencies, default="$")
    product_price = models.FloatField(default=0.00)
    product_discount = models.IntegerField(default=0, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey(ProductCategory, related_name='Category', blank=True, null=True, default=None, on_delete=models.CASCADE) #this
    stock = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.product_name}'

    @property
    def in_stock(self):
        return self.stock > 0

    @property
    def discount_price(self):
        if self.product_discount:
            discount = self.product_price * (self.product_discount / 100)
            discount_price =  self.product_price - discount
            decimal_point_index = str(discount_price).find('.')
            
            decimal_places_count = len(str(discount_price)) - decimal_point_index - 1
            
            if decimal_places_count >= 3:
                discount_price = round(discount_price, 2)
            return discount_price


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        return super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("product_view", kwargs={
            'slug': self.slug
        })



class ProductImg(models.Model):
    product_img = models.ImageField(default='product_default.jpg', upload_to='product_pics')
    is_carousel_active = models.CharField(max_length=10, null=True, blank=True)
    product = models.ForeignKey(ProductModel, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'


    def save(self, *args, **kwargs):
        product_img_length = ProductImg.objects.filter(product=self.product).count()
        if product_img_length < 1:
            self.is_carousel_active = "active"
        else:
            self.is_carousel_active = "not_active"
        return super().save(*args, **kwargs)






class OrderProduct(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name



class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)

    billing_address = models.ForeignKey(
        Address, related_name='billing_address', blank=True, null=True, on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_address', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"

    # def get_raw_subtotal(self):
    #     total = 0
    #     for order_item in self.items.all():
    #         total += order_item.get_raw_total_item_price()
    #     return total

    # def get_subtotal(self):
    #     subtotal = self.get_raw_subtotal()
    #     return "{:.2f}".format(subtotal / 100)

    # def get_raw_total(self):
    #     subtotal = self.get_raw_subtotal()
    #     # add tax, add delivery, subtract discounts
    #     # total = subtotal - discounts + tax + delivery
    #     return subtotal

    # def get_total(self):
    #     total = self.get_raw_total()
    #     return "{:.2f}".format(total / 100)

