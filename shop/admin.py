from django.contrib import admin
from .models import Category, Product



class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')


    
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')



# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)