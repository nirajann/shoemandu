from itertools import product
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Account.models import *
from Store.forms import ProductForm
from Store.models import *
from polls.models import *
from django.contrib import messages

def adminmanage(request):
    customers = signupascustomer.objects.all()
    customer=signupascustomer.objects.all().count()
    product=Product.objects.all().count()
    context  = {
        'customers': customers,'customer':customer,'product':product
        }
    return render(request, 'Adminboard/Dashboard.html',context)


def account(request):
    customers = signupascustomer.objects.all()
    context  = {
        'customers': customers
        }
    return render(request, 'Adminboard/Account.html',context)


def orders(request):
    return render(request, 'Adminboard/orders.html')


def productstore(request):
    customers = Product.objects.all()
    context  = {
        'customers': customers
        }
    return render(request, 'Adminboard/Store.html',context)

def editproduct(request, pk):
    products = Product.objects.get(id=pk)
    category = Category.objects.all()
    context  = {
        'products': products,'category' : category
      }
    return render(request, 'Adminboard/updateproduct.html',context)

def updateproduct(request, pk):
    product=Product.objects.get(id=pk)
    form=ProductForm(request.POST,request.FILES,instance=product)
    form.save()
    return redirect("/")



def category(request):
    customers = Product.objects.all()
    context  = {
        'customers': customers
        }
    return render(request, 'Adminboard/Store.html',context)    

 