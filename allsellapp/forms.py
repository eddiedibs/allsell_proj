from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class UserRegistrationForm(UserCreationForm):
        email = forms.EmailField()
        first_name = forms.CharField(max_length=30, required=False)
        last_name = forms.CharField(max_length=30, required=False)

        class Meta:
                #'model' Dictates where to save the form fields above. In this case, it is saved in registration_model db
                model = User
                #'fields' specifies the fields that are in Post
                fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']