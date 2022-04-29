from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image


class Product_category(models.Model):
    categories = [
        ('Clothes & Accesories', "clothes and accesories"),
        ('Computers, Tablets and IT Accessories', "PC, Tablets and stuff"),
        ('Toys & Games', "Toys and Games"),
        ('Bikes and Automobiles', "Cars and bikes"),
    ]

    color_tags = [
        ('pink-paradise', "pink"),
        ('dark-pastel-green', "pastel green"),
        ('navy-blue', "Navy blue"),
        ('jasmine', "Jasmine"),
    ]




    category = models.CharField(max_length=225, choices=categories, default='Category_test')
    color_tag = models.CharField(max_length=225, choices=color_tags, default='color_test')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.category

    # def get_absolute_url(self):
    #     return reverse('category_detail', kwargs={'slug': self.slug})



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
    img_quantity = models.IntegerField(default=0)
    slug = models.SlugField()
    categories = models.ForeignKey(Product_category, related_name='Category', blank=True, null=True, default=None, on_delete=models.CASCADE) #this

    def __str__(self):
            return f'{self.prod_name} by {self.user.username}'


    def get_absolute_url(self):
        return reverse("products:product_view", kwargs={
            'slug': self.slug
        })


    def img_indicators(self):
        ind_list = []
        for i in range(self.img_quantity):
            ind_list.append(i)
            

        return ind_list

class Product_imgs(models.Model):
    prod_img_title = models.CharField(max_length=40)
    prod_img = models.ImageField(default='product_default.jpg', upload_to='product_pics')
    is_carousel_active = models.CharField(max_length=10)
    item = models.ForeignKey(Product_model, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.prod_img_title} from {self.item}'


    

    # def save(self):
    #     super().save()

    #     imgs = Image.open(self.prod_img.path)

    #     if imgs.height > 300 or imgs.width > 300:
    #         output_size = (300, 300)
    #         imgs.thumbnail(output_size)
    #         imgs.save(self.prod_img.path)