from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image

class Product_model(models.Model):
    currencies = [
    ('$', "US Dollars ($)"), 
    ]



    prod_name = models.CharField(max_length=40)
    prod_desc = models.CharField(max_length=100)
    currency = models.CharField(max_length=5, choices=currencies, default="$")
    prod_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    prod_img = models.ImageField(default='product_default.jpg', upload_to='product_pics')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
            return f'{self.prod_name} by {self.user.username}'


    def get_absolute_url(self):
        return reverse("products:product_view", kwargs={
            'slug': self.slug
        })

        
    def save(self):
        super().save()

        imgs = Image.open(self.prod_img.path)

        if imgs.height > 300 or imgs.width > 300:
            output_size = (300, 300)
            imgs.thumbnail(output_size)
            imgs.save(self.prod_img.path)