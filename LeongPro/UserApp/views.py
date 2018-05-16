from django.shortcuts import render, redirect
from . import models
from hashlib import sha1


# Create your views here.

def aa(request):
    return render(request, 'cart.html')


def register(request):
    return render(request, 'register.html')


def getUname(uname):
    user = models.UserInfo().objects.get(uname)
    if user is None:
        return False
    else:
        return True


def register_handle(request):
    # 接受用户输入的请求
    uname = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    upwd2 = request.POST.get('cpwd')
    uemail = request.POST.get('enail')

    if upwd != upwd2:
        return redirect('/user/register')
    s1 = sha1()
    s1.update(upwd.encode('utf8'))
    upwd3 = s1.hexdigest()

    user = models.UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')


def login(request):
    return render(request, 'login.html')

def user_center_info(request):
    return render(request,'user_center_info.html')

def user_center_order(request):
    return render(request,'user_center_order.html')

def user_center_site(request):
    return render(request,'user_center_site.html')
