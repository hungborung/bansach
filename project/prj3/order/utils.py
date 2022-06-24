import datetime
import os
from random import randint
from cart.cart import Cart

from order.models import Order, OrderItem

def checkout(request, first_name, last_name, phone, email, address, zipcode, place):
    
    order = Order(first_name=first_name, last_name=last_name, phone=phone, email=email, address=address, zipcode=zipcode, place=place)

    if request.user.is_authenticated:
        order.user = request.user
    order.save()

    cart = Cart(request)

    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

    return order.id