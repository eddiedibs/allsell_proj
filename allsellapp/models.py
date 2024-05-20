from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image








class HomeBanner(models.Model):

    time_periods = [
        ('January', 'January_banners'),
        ('February', 'February_banners'),
        ('March', 'March_banners'),
        ('May', 'May_banners'),
        ('June', 'June_banners'),
        ('July', 'July_banners'),
        ('August', 'August_banners'),
        ('September', 'September_banners'),
        ('November', 'November_banners'),
        ('December', 'December_banners'),
    ]


    banner_title = models.CharField(max_length=40)
    banner_list_date = models.CharField(max_length=30, choices=time_periods, default="Test_period")

    def __str__(self):
        return f"Home Banner {self.banner_title}"




class BannerImgs(models.Model):
    product_img = models.ImageField(default='product_default.jpg', upload_to='product_pics')
    banner_item = models.ForeignKey(HomeBanner, null=True, blank=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Home Banner {self.product_img.file.name.split('/')[-1]}"

