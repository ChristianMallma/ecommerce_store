from .models import Product, Category

from django.shortcuts import render

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        'products': product_list,
        'categories': category_list
    }

    return render(request, 'index.html', context)


def products_by_category(request, category_id):
    category_object = Category.objects.get(pk=category_id)
    product_list = category_object.product_set.all()
    category_list = Category.objects.all()

    context = {
        "products": product_list,
        "categories": category_list
    }

    return render(request, 'index.html', context)


def products_by_name(request):
    name = request.POST['name']

    product_list = Product.objects.filter(name__contains=name.upper())
    category_list = Category.objects.all()

    context = {
        "products": product_list,
        "categories": category_list
    }

    return render(request, 'index.html', context)
