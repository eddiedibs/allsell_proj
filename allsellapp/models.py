from django.db import models
from django.contrib.auth.models import User

class Product_model(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_desc = models.CharField(max_length=100)
    prod_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    # def __str__(self):
    #     return self.firstName + ' ' + self.lastName