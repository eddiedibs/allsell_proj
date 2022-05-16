from django.contrib import admin
from django.urls import path
from . import views
from users_allsell import views as user_views
from products import views as product_views

urlpatterns = [
    # path('', views.home, name='home_view'),
    path('', views.HomeListView.as_view(template_name='allsellapp/home.html'), name='home_view'),


]
