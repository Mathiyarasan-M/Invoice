from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Inv import models
from Inv.models import *
# Create your views here.
def user_login(request):
    if request.method == "POST":
       username=request.POST.get('username')
       password=request.POST.get('password')
       user =authenticate(username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect("/")
           
    return render(request,'login.html')


def user_register(request):
    if request.method =="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        dateofbirth=request.POST.get('DOB')
        gender=request.POST.get('gender')
        address=request.POST.get("address")
        dateofjoin=request.POST.get('DOJ')  
        phone_number=request.POST.get('phone_number')
        phone2number=request.POST.get('phone2number')
        myfile=request.POST.get('myfile')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                    return redirect('user_register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    data=Users(username = username,  phonenumber= phone_number)
                    data.save()

                    our_user=authenticate(username=username,password=password)
                    if our_user is not None:
                        login(request,user)
                        return redirect('/')
        else:
            print("Error here...")
            return redirect('user_register')
    return render(request,'register.html')
def user_logout(request):
    logout(request)
    return redirect('/')