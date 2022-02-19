from dataclasses import field
from django import forms 
from .models import *

class FilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('name','image','description','price')