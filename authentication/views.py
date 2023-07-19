from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages

# from .models import user


#dashboard
def dash(request):
    return render(request, 'dash.html')


#sign up page
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #check usernames and password already exist or not
        if User.objects.filter(username=username).exists():
             messages.info(request,'username already exists')
             return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists')
            return redirect('signup')
        else:
            user= User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print('User created successfully')
            return redirect('log')  # Redirect to the login page
        
    #if request.method is 'GET'    
    else:
         return render(request,'signup.html')


#login page
def log(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(request, username=username,password=password)

            if user is not None:
                auth.login(request, user)
                print('User logged in successfully')
                return redirect('dash')  # Redirecting to the dashboard page after successful login
            
            else:
                messages.info(request,'Invalid username or password')
                return redirect('log')# Redirecting to the same login page after unsuccessful login

    #if request.method is GET            
    return render(request, 'log.html')