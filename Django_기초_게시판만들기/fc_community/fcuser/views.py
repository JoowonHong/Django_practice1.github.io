from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Fcuser
from django.contrib.auth.hashers import make_password,check_password
from .forms import LoginForm
# Create your views here.

def home(request):
    return render(request,'home.html')
    

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user']= form.user_id
    
            #session
            return redirect('/')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})



def register(request):
    if request.method =="GET":
        return render(request,'register.html')
    elif request.method=="POST":
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        re_password=request.POST.get('re-password',None)
        e_mail = request.POST.get('useremail',None)
      
        res_data={}

        if not (username and password and re_password and e_mail):
             res_data['error'] ='모든 항목을 입력해야 합니다!'
        elif password!=re_password:
            res_data['error'] ='비밀번호가 다릅니다!'
        else:
            fcuser= Fcuser(
            username=username,
            useremail=e_mail,
            password=make_password(password)
            )

            fcuser.save()

        return render(request,'register.html',res_data)