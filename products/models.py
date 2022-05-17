from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image
from .categories_and_colortags import categories, color_tags




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



    slug = models.SlugField(unique=True)
    prod_name = models.CharField(max_length=40)
    prod_desc = models.TextField(max_length=500)
    currency = models.CharField(max_length=5, choices=currencies, default="$")
    prod_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    prod_discount_price = models.FloatField(blank=True, null=True)
    prod_img = models.ImageField(default='product_default.jpg', upload_to='product_pics')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey(ProductCategory, related_name='Category', blank=True, null=True, default=None, on_delete=models.CASCADE) #this

    def __str__(self):
        return f'{self.prod_name} by {self.user.username}'


    def get_absolute_url(self):
        return reverse("product_view", kwargs={
            'slug': self.slug
        })






class ProductImg(models.Model):
    prod_img_title = models.CharField(max_length=40)
    prod_img = models.ImageField(default='product_default.jpg', upload_to='product_pics')
    is_carousel_active = models.CharField(max_length=10)
    item = models.ForeignKey(ProductModel, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.prod_img_title} from {self.item}'








class OrderProduct(models.Model):
    item = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.prod_name



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

