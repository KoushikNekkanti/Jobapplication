from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .urls import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
def index(request):
    return render(request,'main/index.html')
    # return HttpResponse('hello')
def dasha(request):
          if request.user.is_authenticated:
               return render(request,'main/dasha.html')
          else:
               return redirect('signin')
def dashb(request):
          if request.user.is_authenticated:
               return render(request,'main/dashb.html')
          else:
               return redirect('signin')
def signup(request):
    if request.method=="POST":
          username=request.POST['username']
          firstname=request.POST['firstname']
          lastname=request.POST['lastname']
          email=request.POST['email']
          password=request.POST['password']
          confirmpassword=request.POST['confirmpassword']
          rec= request.POST.get('user_type') 
          if User.objects.filter(username=username).exists():
               messages.error(request,"Username already exist!")
               return redirect('signup')
          if User.objects.filter(email=email).exists():
               messages.error(request,"Email already exist!")
               return redirect('signup')
          if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
          if password !=confirmpassword:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
          if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
          user=User.objects.create_user(username,email,password)
          user.first_name=firstname
          user.last_name=lastname
          user.is_staff=rec=="recruiter"
          user.is_active=True
          user.save()

          messages.success(request,"Your Account details has been taken, To activate Account verify your email id")
          sub="Welcome to Our Website"
          return redirect("signin")  
    return render(request,'main/signup.html')
def signin(request):
    if request.method == 'POST':

          username=request.POST['username']
          password=request.POST['password']
          user=authenticate(username=username,password=password)
          
          if user is not None:
               login(request,user)
               f=user.first_name
               user_type=user.is_staff
               if user_type:
                   return redirect("dasha")   
               return redirect("dashb")  
                   
          else:
               print('jj')
               messages.error(request,"Enter correct Credentials")
               return redirect("signin")
    return render(request,'main/signin.html')