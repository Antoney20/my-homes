from django.shortcuts import render,redirect

import requests


# Create your views here.

def index(request):
    return render(request, 'myhome/index.html')
    
def register(request):
    return render(request, 'myhome/register.html')

def confirm_email(request):
    return render(request, 'myhome/register.html')
    


