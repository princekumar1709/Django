from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def dash(request):
    return render(request, 'dash.html')

def login_view(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         if user.is_superuser:
    #             # Admin login successful
    #             login(request, user)
    #             return redirect('admin_dashboard')  # Redirect to the admin dashboard
    #         else:
    #             # User login successful
    #             login(request, user)
    #             return redirect('user_dashboard')  # Redirect to the user dashboard
    #     else:
    #         # Invalid credentials
    #         return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def register(request):
    return render(request,'register.html')
