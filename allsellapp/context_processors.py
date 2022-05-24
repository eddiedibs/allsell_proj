from products.models import Order


def base_processors(request):
 orders = Order.objects.all()            
 return {'orders': orders}