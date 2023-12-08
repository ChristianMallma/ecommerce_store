from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('productsByCategory/<int:category_id>', views.products_by_category, name='products_by_category'),
    path('productsByName/', views.products_by_name, name='products_by_name')
]