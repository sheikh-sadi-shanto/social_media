from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from userapp.form import Loginform,Registerform
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
        form=Loginform()
        if form.is_valid():
            username=form.cleaned_data('username')
            password=form.cleaned_data('password')
    else:
        form=Loginform()
    return render(request,'login.html',{'l':form})

def register(request):
    if request.method=='POST':
        rform=Registerform(request.POST)
        if rform.is_valid():
            us=rform.cleaned_data.get('username')
            em=rform.cleaned_data.get('email')
            password=rform.cleaned_data.get('password')
            password1=rform.cleaned_data.get('password1')


            if User.objects.filter(username=us).exists():
                messages.add_message(request,messages.INFO,'username already exist')
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.add_message(request,messages.INFO,'email already exist')
                return redirect('register')
            elif password == password1:
                user=User.objects.create(username=us,email=em,password=password)
                user.save()
            else:
                print('password not matched')
                return redirect('regitser')
    else:
        rform=Registerform()
    return render(request,'register.html',{'rform':rform})
