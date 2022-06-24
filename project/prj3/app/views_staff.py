from django.shortcuts import render, redirect
from .models import *
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from order.models import Order, OrderItem
import math
from datetime import datetime

@login_required
def staffHome(request):
    return render(request, 'staff/home.html')


@login_required
def listCategory(request):
    categoryList = Category.objects.all()
    paginator = Paginator(categoryList, 2)
    page = request.GET.get('page')
    
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)


    context = {
        'categoryList' : categoryList,
        'page' : 'page',
        'categories' : categories,
        'total' : paginator.count,

    }
    return render(request, 'staff/category/list.html', context)

@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/staff/list-category'
    query_pk_and_slug = False
    template_name = 'staff/category/form.html'

@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/staff'
    template_name = 'staff/category/form.html'

@login_required
def deleteCategory(request, pk):
    c = Category.objects.get(pk=pk)

    try:
        child = Category.objects.filter(cat_parent=c.pk).delete()
    except Category.DoesNotExist:
        child = None
        
    try: 
        p = Product.objects.filter(category=c.pk).delete()
    except Product.DoesNotExist:
        p = None

   
    c.delete()
    
    return redirect('list-category')


@login_required
def listProduct(request):
    productList = Product.objects.all()
    paginator = Paginator(productList, 2)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


    context = {
        'productList' : productList,
        'page' : 'page',
        'products' : products,
        'total' : paginator.count,

    }
    return render(request, 'staff/product/list.html', context)


@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = '/staff/list-product'
    query_pk_and_slug = False
    template_name = 'staff/product/form.html'

@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = '/staff/list-product'
    template_name = 'staff/product/form.html'

@login_required
def deleteProduct(request, pk):
    p = Product.objects.get(pk=pk)
    p.delete()
    return redirect('list-product')

@login_required
def listOrder(request):
    orderList = Order.objects.all()
    paginator = Paginator(orderList, 10)
    page = request.GET.get('page')
    
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    status = Status.objects.all()
    context = {
        'orderList' : orderList,
        'page' : 'page',
        'orders' : orders,
        'total' : paginator.count,
        'status': status,

    }
    return render(request, 'staff/order/list.html', context)

@login_required
def viewOrder(request, pk):
    order = Order.objects.get(pk=pk)
    orderDetail = OrderItem.objects.filter(order=pk)
    
    context = {
        'orderDetail': orderDetail,
        'order': order,
        
    }
    return render(request, 'staff/order/detail.html', context)


@login_required
def confirmOrderDeliver(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Status.objects.get(id=2)
    order.deliver_date = datetime.now()
    order.save()
    
    return redirect('list-order')

@login_required
def cancelOrder(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Status.objects.get(id=3)
    order.save()
    return redirect('list-order')

@login_required
def listTerm(request):
    termList = TermOfUse.objects.all()
    context = {
        'termList' : termList,
    }
    return render(request, 'staff/termofuse/list.html', context)

@method_decorator(login_required, name='dispatch')
class TermCreateView(CreateView):
    model = TermOfUse
    fields = '__all__'
    success_url = '/staff/list-term'
    query_pk_and_slug = False
    template_name = 'staff/termofuse/form.html'

@method_decorator(login_required, name='dispatch')
class TermUpdateView(UpdateView):
    model = TermOfUse
    fields = '__all__'
    success_url = '/staff/list-term'
    template_name = 'staff/termofuse/form.html'