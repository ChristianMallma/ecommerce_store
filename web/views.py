from .models import Product, Category
from .cart import Cart

from django.shortcuts import render, get_object_or_404

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


def detail_product(request, product_id):
    product_object = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product_object
    }

    return render(request, 'producto.html', context)


# Shopping car
def shopping_cart(request):
    return render(request, 'carrito.html')


def add_product_to_cart(request, product_id):
    quantity = 1
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])

    product_object = Product.objects.get(pk=product_id)

    shopping_cart_object = Cart(request)
    shopping_cart_object.add(product=product_object,
                             quantity=quantity)

    print('LINE 68', request.session.get('cart'))
    return render(request, 'carrito.html')
