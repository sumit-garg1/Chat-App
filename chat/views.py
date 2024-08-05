from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate,login as auth_login
# Create your views here.
def base(request):
    return render(request,"base.html")
def home(request):
    return render(request,"home.html")
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            messages.error(request,"invalid login or password")  
            return render(request, 'login.html')  # Add this line
    return render(request,'login.html')    
def signup(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')  # Corrected field name
        if password != confirm_password:
            messages.error(request, "Password and confirm password do not match")
        else:
            my_user = User.objects.create_user(uname, email, password)
            my_user.save()
            return redirect('login')
    return render(request, "signup.html")
def login_signup(request):
    return render(request,'home.html')
def signup_login(request):
    return render(request,'signup.html')
def logout(request, slug):
    auth_logout(request)
    return redirect('/')