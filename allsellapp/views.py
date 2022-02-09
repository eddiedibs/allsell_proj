from django.shortcuts import render




def home(request):
    return render(request, 'allsellapp/home.html')

# Create your views here.
