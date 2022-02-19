from itertools import product
from unicodedata import category
from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','category','price',"available"]
    prepopulated_fields = {"slug":("name",)}