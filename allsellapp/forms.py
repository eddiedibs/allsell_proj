from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import registration_model




class UserRegistrationForm(forms.ModelForm):
        firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First name'}))
        lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last name'}))
        email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email address'}))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))

        class Meta:
                #'model' Dictates where to save the form fields above. In this case, it is saved in registration_model db
                model = registration_model
                #'fields' specifies the fields that are in Post
                fields = ['firstName', 'lastName', 'email', 'password1']