from django.shortcuts import render,HttpResponse,redirect
from .forms import Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

# Create your views here.

def register(request):
    register=Register()
    if request.method =='POST':
        register=Register(request.POST)
        if register.is_valid():
            # register.save()
            un= register.cleaned_data['username']
            email=register.cleaned_data['email']
            password=register.cleaned_data['password2']
            print(un,password)
            a=User(username=un,email=email)
            a.set_password(password)
            a.save()
            print(a)

            pass
            # return redirect('login')
    return render(request,'register.html',{'register':register})

def log_in(request):
     
     if request.method=='POST':
        un=request.POST['un']
        # ua=request.POST.get('fa')
        # la=request.POST['ln']
        password=request.POST.get('pwd')
        # password=request.POST['pwd']
        # print(ua,la)
        try:
            user=User.objects.get(username=un)
            print("user found",user)
            # print('User found',user)
        except Exception as e:
            return HttpResponse(f"user not found {e}")
        user=authenticate(request,username=un,password=password)
        # print(user)
        if user is not None:
            login(request,user)
            print('login successful')
            return redirect('home')

     return render(request,'login.html')

@login_required(login_url="login")

def index(request):
    user=request.user
    return render(request,'index.html',{'user':user})
def log_out(request):
    logout(request)
    return redirect('login')
