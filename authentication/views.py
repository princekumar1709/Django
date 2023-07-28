from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import pandas as pd
from.models import ExcelData
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

# logout page
def logout(request):
     auth.logout(request)
     return redirect('dash')


def upload(request):
    return render(request,'upload.html')

def visual(request):
    if request.method == 'POST' and request.FILES.get('excelFile'):
        excel_file = request.FILES['excelFile']

        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(excel_file)

        columns = df.columns.to_list()

        # Convert DataFrame to JSON (List of dictionaries)
        data_list = df.to_dict(orient='records')

        # Save data to the database
        ExcelData.objects.create(data=data_list)
        return render(request, 'visual.html',{'cols':columns})
    else:
        return redirect(request,'upload')