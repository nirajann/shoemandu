from django.shortcuts import render
from .models import *
from Account.forms import*

# Create your views here.
from django.shortcuts import render

def customer_order(request):
    customers = signupascustomer.objects.get(username=request.session['username'])
    context  = {
        'customers': customers,
        }
    return render(request,'store/order.html',context)