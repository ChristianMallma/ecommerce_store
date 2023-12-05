from django.contrib import admin
from .models import Category, Product

# Register your models here.
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'registration_date')
    list_editable = ('price',)
