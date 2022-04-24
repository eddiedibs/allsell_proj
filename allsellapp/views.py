from django.shortcuts import render
from products.models import Product_model




def home(request):
    context = {
        'products': Product_model.objects.all()
    }


    return render(request, 'allsellapp/home.html', context)

