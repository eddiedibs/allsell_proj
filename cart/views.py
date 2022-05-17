from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from products.models import ProductModel
from allsellapp.models import HomeBanner





class CartTemplateView(TemplateView):
    template_name = 'cart.html'

    # def get_context_data(self, **kwargs):

    #     products = self.model[0].objects.all()
    #     banners = self.model[1].objects.all().filter(banner_title='Clothing and Automobile Promo').first()

    #     all_data = {
    #         'products': products,
    #         'banners': banners,
    #     }

    #     return all_data


    # def get(self, request):
        
    #     return render(request, self.template_name, context=self.get_context_data())


# def home(request):
#     context = {
#         'products': ProductModel.objects.all(),
#         'banners': Home_banner.objects.all().filter(banner_title='Clothing and Automobile Promo').first(),
#     }


#     return render(request, 'allsellapp/home.html', context)

