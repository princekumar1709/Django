from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from .models import user

def dash(request):
    return render(request, 'dash.html')

def log(request):
    return render(request, 'log.html')

def register(request):
    return render(request,'register.html')


def signup(request):
    if request.method == 'POST':
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            phone=request.POST['phone']
            address=request.POST['address']

            user1= User.objects.create_user(name=name, email=email, password=password, phone=phone,address=address)
            print(user1)
            print('user created')
            return redirect('/')
    
    else:
         return render(request,'signup.html')
