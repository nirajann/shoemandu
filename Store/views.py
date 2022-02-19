from django.shortcuts import render

from django.conf import settings

from .models import Product
from .models import Category
from Account.models import *
from .forms import *
from django.db.models import Q



def homepage(request):
    return render(request,'Home/homepage.html')


def store(request):
    customers = signupascustomer.objects.get(username=request.session['username'])
    context  = {
        'products':Product.objects.all(),
        'form':FilterForm(),
        'customers': customers
        }
    
    return render(request,'store/store.html',context)

def profile(request):
    customers = signupascustomer.objects.get(username=request.session['username'])
    context  = {
        'customers': customers
        }
    
    return render(request,'store/profile.html',context)    


def SearchView(request):
    query = request.GET['query']
    products = Product.objects.filter(name__icontains =query)
    context ={ 'products':products}
    return render(request,'Home/search.html',context)    



def searchresult(request):
    query = request.GET['query']
    products = Product.objects.filter(name__icontains =query)
    context ={ 'products':products}
    return render(request,'store/search.html',context)        