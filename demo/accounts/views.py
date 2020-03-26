from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        password = request.POST['password']
        conf_password = request.POST['confirm_pass']
        username = request.POST['username']

        if User.objects.filter(username = username):
            messages.info(request,'Username already exists')
            return redirect('register')
        elif User.objects.filter(email = email):
            messages.info(request,'Email already exists')
            return redirect('register')
        elif password != conf_password:
            messages.info(request,'Password does not match')
            return redirect('register')
        else:
            user = User.objects.create_user(username = username, email= email, password= password, last_name = last_name, first_name= first_name)
            user.save()
            print('user created')
            return redirect('/travello')
    else:
        return render(request,'register.html')



def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/travello')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/travello')


def satara(request):
    if not request.user.is_authenticated:
        return redirect('/travello')
    else:
        return redirect('satara')