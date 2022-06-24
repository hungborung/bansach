from django.shortcuts import render
from .cart import *
from django.conf import settings
# Create your views here.
def cart_detail(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        url = '/%s/%s/' %('product', product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'image': '%s', 'url': '%s', 'num_available': '%s',}," % (product.id, product.name, product.price_sell, item['quantity'], item['total_price'], product.image.url , url, product.num_available )
        productsstring = productsstring + b

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        phone = request.user.phone
        email = request.user.email
    else:
        first_name = last_name = phone = email = ''

    context = {
        'cart': cart,
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email,
        'pub_key': settings.STRIPE_API_KEY_PUBLISHABLE,
        'productsstring': productsstring.rstrip(',')
    }
    return render(request, 'cart.html', context)

def success(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'success.html')



