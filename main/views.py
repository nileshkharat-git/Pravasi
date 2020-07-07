from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.messages import success,info,error
from .forms import RegiForm
from .models import accounts
from Pravasi.views import home
def userSignup(request):
    context={}
    if request.POST:
        form=RegiForm(request.POST)
        if form.is_valid():
            form.save()
            success(request,'User created successfully')
            return redirect('/user/login/')
        else:
            error(request,'User Signup Failed')
            return redirect('/user/signup/')
    else:
        form=RegiForm()
    context['form']=form
    return render(request,'mypages/signup.html',context)

def userLogin(request):
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        if user:
            login(request,user)
            info(request,'now you are logged in')
            return redirect(home)
        else:
            error(request,'Authentication failed')
            redirect('/user/login')
    return render(request,'mypages/login.html')

def userlogout(request):
    logout(request)
    return render(request,'mypages/logout.html')