from django.shortcuts import render, redirect
from . import models
from hashlib import sha1

# Create your views here.
def cart(request):
    return render(request,'cart.html')

def detail(request):
    return render(request,'detail.html')
def index(request):
    return render(request,'index.html')

def list(request):
    return render(request,'list.html')

# def index(request):
#     return render(request,'index.html')

