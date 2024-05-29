from products.models import Order

def get_or_create_order(request, is_completed):
    """
    Retrieve or create an order for the given user and store the order ID in the session.
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order_id = request.session.get('order_id')
        if order_id:
            try:
                order = Order.objects.get(id=order_id, customer=customer, completed=is_completed)
            except Order.DoesNotExist:
                order = Order.objects.create(customer=customer, completed=is_completed)
                request.session['order_id'] = str(order.id)
        else:
            order, created = Order.objects.get_or_create(customer=customer, completed=False)
            request.session['order_id'] = str(order.id)
        return order
    else:
        return None
