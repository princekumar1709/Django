from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

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
        user= User.objects.create_user(username=username, email=email, password=password)
        if user:
            print('User created successfully')
            user.save()
            return redirect('log')  # Redirect to the login page
        else:
            return redirect('signup.html') #redirect to the signup page
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
                return redirect('dash')  # Redirect to the dashboard page after successful login
            else:
                return HttpResponse('Invalid username or password')
    return render(request, 'log.html')