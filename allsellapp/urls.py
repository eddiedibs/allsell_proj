from django.contrib import admin
from django.urls import path
from . import views
from users_allsell import views as user_views

urlpatterns = [
    path('', views.home, name='home_view'),
]
