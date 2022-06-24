from django.shortcuts import render, get_object_or_404
from app.models import Publisher, Product
# Create your views here.


def publisher(request, slug):
    publisher = Publisher.objects.get(slug=slug)

    product = Product.objects.filter(publisher=publisher.id)

    context = {
        'publisher': publisher,
        'product': product,
    }

    return render(request, 'publisher.html', context)
