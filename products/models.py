import uuid
import locale

# Set the locale to English (United States)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image
from .categories_and_colortags import categories, color_tags
from django.utils.text import slugify
from djmoney.models.fields import MoneyField
from .utils import get_currency_symbol

class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_first_name = models.CharField(default="First name", max_length=100)
    user_last_name = models.CharField(default="Last name", max_length=100)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)

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
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    slug = models.SlugField(unique=True, blank=True, default=None)
    product_name = models.CharField(max_length=40)
    product_description = models.TextField(max_length=500)
    product_price = MoneyField(max_digits=14, default=0.00, decimal_places=2, default_currency='USD')
    product_discount = models.IntegerField(default=0, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey(ProductCategory, related_name='Category', blank=True, null=True, default=None, on_delete=models.CASCADE) #this
    stock = models.IntegerField(default=1)


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






class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email}'

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

    @property
    def get_customer_order(self):
        return self.order_set.filter(customer=self).first().get_cart_amount_of_items


class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
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
        return f"ORDER-{self.id}"

    @property
    def get_cart_total(self):
        orderproducts = self.orderproduct_set.all()
        total = sum([locale.atof(product.total_amount[1:])  for product in orderproducts ])
        if orderproducts.first() == None and total == 0:
            return ""
        currency = str(orderproducts.first().total_amount)[0]
        return currency + f'{total:,.2f}'

    @property
    def get_cart_amount_of_items(self):
        orderproducts = self.orderproduct_set.all()
        total = sum([order_product.quantity for order_product in orderproducts])
        return total


class OrderProduct(models.Model):
    product = models.ForeignKey(ProductModel, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.product_name



    @property
    def is_amount_in_stock(self):
        return self.quantity < self.product.stock

    @property
    def amount_in_stock(self):
        return self.product.stock

    @property
    def total_amount_without_discount(self):
        return str(self.product.product_price * self.quantity)

    @property
    def total_amount(self):
        if self.product.discount_price:
            total = self.product.discount_price * self.quantity
        else:
            total = self.product.product_price * self.quantity
        return get_currency_symbol(total.currency.code) + f'{total.amount:,.2f}'
        