from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('productsByCategory/<int:category_id>', views.products_by_category, name='products_by_category'),
    path('productsByName/', views.products_by_name, name='products_by_name'),
    path('product/<int:product_id>', views.detail_product, name='detail_product'),
    # Shopping car
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('add_product_to_cart/<int:product_id>', views.add_product_to_cart, name='add_product_to_cart')
]