from django.db import models
from django.contrib.auth.models import User

class registration_model(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


    def __str__(self):
        return self.firstName + ' ' + self.lastName