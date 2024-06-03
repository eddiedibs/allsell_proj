from products.models import Order

def get_or_create_order(obj, is_completed):
    """
    Retrieve or create an order for the given user and store the order ID in the session.
    """
    if obj.request.user.is_authenticated:
        customer = obj.request.user.customer
        if obj.kwargs:
            order_id = obj.kwargs["pk"]
        else:
            order_id = obj.request.session.get('orderId')
        if order_id:
            try:
                order = Order.objects.get(id=order_id, customer=customer, completed=is_completed)
            except Order.DoesNotExist:
                order = Order.objects.create(customer=customer, completed=is_completed)
                obj.request.session['orderId'] = str(order.id)
        else:
            order, created = Order.objects.get_or_create(customer=customer, completed=False)
            obj.request.session['orderId'] = str(order.id)
        return order
    else:
        return None
