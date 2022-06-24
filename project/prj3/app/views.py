from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Product, Publisher, Category, ProductReview
from django.views.generic.detail import DetailView
from cart.cart import Cart
from order.models import Order, OrderItem
import random
from heapq import nlargest
import heapq
from datetime import datetime
# Create your views here.

priceList = [
    {'id': 1, 'name': '0đ - 150,000đ', 'max': 150000},
    {'id': 2, 'name': '150,000đ-500,000đ', 'min': 151000, 'max': 500000},
    {'id': 3, 'name': 'Trên 500,000đ', 'min': 501000},
]

def index(request):
    product = Product.objects.filter(is_featured=True)
    listCategory = Category.objects.filter(cat_parent=None)
    cart = Cart(request)

    orders = OrderItem.objects.all()
    
    popular_products = Product.objects.all().order_by('-num_visits')[0:5]
    recently_viewed_products = Product.objects.all().order_by('-last_visit')[0:10]

    counts = {}
    for o in orders:
        pro, qty = o.product, o.quantity
        counts[pro] = counts.get(pro, 0) + qty
    context = {
        'product' : product,
        'listCategory' : listCategory,
        'cart': cart,
        'popular_products': popular_products,
        'recently_viewed_products': recently_viewed_products
    }
    return render(request, 'index.html', context)

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query)
    publisherId = request.GET.get('publisherId')
    publisher = Publisher.objects.all()
    publisherId = int(publisherId) if publisherId else None

    if publisherId:
        products = products.filter(publisher__id=publisherId)

    priceId = request.GET.get('priceId')
    priceId = int(priceId) if priceId else None
    price = priceList[priceId-1] if priceId else {}
    minPrice, maxPrice = price.get('min'), price.get('max')
    if minPrice:
        products = products.filter(price_sell__gte=minPrice)
    if maxPrice:
        products = products.filter(price_sell__lte=maxPrice)


    
    context = {
        'query': query,
        'products': products,
        'publisherId': publisherId,
        'priceId': priceId,
        'priceList': priceList,
        'publisher' : publisher,
    }

    return render(request, 'product-page.html', context)


def categorydetail(request, slug):
    name = request.GET.get('name', '')
    publisherId = request.GET.get('publisherId')
    publisher = Publisher.objects.all()
    category = get_object_or_404(Category, slug=slug)
    product = Product.objects.filter(category=category.id)

    productList = product.filter(name__icontains=name)
    publisherId = int(publisherId) if publisherId else None

    if publisherId:
        productList = productList.filter(publisher__id=publisherId)

    priceId = request.GET.get('priceId')
    priceId = int(priceId) if priceId else None
    price = priceList[priceId-1] if priceId else {}
    minPrice, maxPrice = price.get('min'), price.get('max')
    if minPrice:
        productList = productList.filter(price_sell__gte=minPrice)
    if maxPrice:
        productList = productList.filter(price_sell__lte=maxPrice)

    context = {
        'category': category,
        'product': product,
        'publisher' : publisher,
        'name': name,
        'productList': productList,
        'publisherId': publisherId,
        'priceId': priceId,
        'priceList': priceList,
        
    }
    return render(request, 'category.html', context)


def productdetail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = Cart(request)

 
    related_products = list(product.category.products.filter(parent=None).exclude(id=product.id))
    
    if (len(related_products) >= 3):
        related_products = random.sample(related_products, 3)
    
    if product.parent:
        return redirect('productdetail', slug=product.parent.slug)


    if product.discount > 0:
        priceDiscount = product.price_sell * ((100-product.discount)/100)
    else:
        priceDiscount = product.price_sell
    
    if not product.thumbnail:
        imagesstring = "{'image': '%s'}," % (product.image.url) 
    else:
        imagesstring = "{'thumbnail': '%s','image': '%s'}," % (product.thumbnail.url, product.image.url) 
        for image in product.images.all():
            imagesstring = imagesstring + ("{'thumbnail': '%s', 'image': '%s'}," % (image.thumbnail.url, image.image.url))
          
    
    cart = Cart(request)


    if cart.has_product(product.id):
        product.in_cart = True
    else:
        product.in_cart = False


    
    product.num_visits = product.num_visits + 1
    product.last_visit = datetime.now()
    product.save()

    #add review

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')
        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)
        return redirect('productdetail', slug=slug)
    total_review = ProductReview.objects.filter(product=product.id).count()
    #

    context = {
        'product': product,
        'cart': cart,
        'priceDiscount': priceDiscount,
        'imagesstring': imagesstring,
        'related_products': related_products,
        'total_review': total_review
    }

    return render(request, 'productdetail.html', context)

def help(request):
    return render(request, 'help.html')

def termofuse(request):
    return render(request, 'termofuse.html')
