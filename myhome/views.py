from django.shortcuts import render,redirect

import requests
from django.core.mail import send_mail
from django.conf import settings
from .models import User
import hashlib

# Create your views here.

def index(request):
    return render(request, 'myhome/index.html')
    
def register(request):
    if request.method == 'POST':
        # Processi n the form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            return render(request, 'myhome/register.html', {'error_message': 'Email already registered.'})

        verification_token = hashlib.sha256(f'{email}{username}'.encode()).hexdigest()
        
                # Create a new user object and saving him to the db
        user = User(username=username, email=email, password=password)
        user.save()

        # Send the verification email to the user
        subject = 'Email Verification'
        message = f'Hi {username}, Please click the link to verify your email: {settings.BASE_URL}/verify/{verification_token}/'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        return redirect('index')
        
        return redirect('success')
    
    return render(request, 'myhome/register.html')

def verify_email(request, verification_token):
    try:
        # Find the user with the given verification token
        user = User.objects.get(is_email_verified=False, verification_token=verification_token)
        # Mark the user as verified
        user.is_email_verified = True
        user.save()
    except User.DoesNotExist:
        return HttpResponse('Failed to verify email')
    return redirect('index')
    


