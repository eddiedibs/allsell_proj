from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from products.models import Product_model, Home_banner




class HomeListView(ListView):
    model = Product_model, Home_banner
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        products = self.model[0].objects.all()
        banners = self.model[1].objects.all().filter(banner_title='Clothing and Automobile Promo').first()

        all_data = {
            'products': products,
            'banners': banners,
        }

        return all_data


    def get(self, request):
        
        return render(request, self.template_name, context=self.get_context_data())


# def home(request):
#     context = {
#         'products': Product_model.objects.all(),
#         'banners': Home_banner.objects.all().filter(banner_title='Clothing and Automobile Promo').first(),
#     }


#     return render(request, 'allsellapp/home.html', context)

