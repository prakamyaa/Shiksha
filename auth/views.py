from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    return render(request,'auth/index.html')
def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.email=email
        myuser.save()
        messages.success(request,'Registration Successful')
        return redirect('signin')
    return render(request,'auth/signup.html')
def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)

            return render(request,'authentication/index.html')
        else:
            messages.error(request,'Username or Password is wrong')
            return redirect('home')
    return render(request,'auth/signin.html')


def signout(request):
    pass
    



    return render(request,'auth/signup.html')
def signin(request):
    return render(request,'auth/signin.html')
def signout(request):
    pass

    
