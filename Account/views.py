from genericpath import exists
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import*
from .forms import*
from django.contrib.auth import logout
from django.contrib import messages

def signupcustomer(request):
    print(request)
    if request.method =='POST':
            form = customer(request.POST)
            if form.is_valid():
                if signupascustomer.objects.filter(username=request.POST['username']).exists():
                    messages.error(request,"username already exists")
                    return render(request, 'Home/signup.html')
                else:
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request,"you can now login " + user)
                    print(form)
            return redirect('/login')     
                
    return render(request, 'home/signup.html')

def login(request):
    if request.method=='POST':
        print(request)
        username=request.POST["username"]
        password=request.POST["password"]
     
        customers=signupascustomer.objects.get(username=username,password=password)
        request.session['username']=request.POST['username']
        request.session['id']=customers.id
        return redirect ('/store')
    else:
        form= customer()
        print("invalid")
    return render(request,"Home/login.html",{'form':form})  


def logout_view(request):
 logout(request)
 return  redirect('/')