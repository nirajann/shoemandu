from django.contrib import admin

# Register your models here.
from itertools import product
from unicodedata import category
from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(updateCategory)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

@admin.register(updateProduct)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','category','price',"available"]
    prepopulated_fields = {"slug":("name",)}