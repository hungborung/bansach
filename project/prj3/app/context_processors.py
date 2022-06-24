from .models import Category

def menu_categories(request):
    categories = Category.objects.filter(cat_parent = None)

    return {'menu_categories': categories}
    