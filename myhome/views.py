from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
from django.core.mail import send_mail
from django.conf import settings
from .models import User, Profile, SubmitProperty
from .forms import SubmitPropertyForm
from django.http import HttpResponse
import hashlib
# property detail
from django.http import Http404
# Create your views here.

@login_required
def index(request):
    properties = SubmitProperty.objects.all()
    user = request.user
    
    context = {
        'properties': properties,
        'user': user,   
        'logged_in': True,  
    }
    if user.is_authenticated:
        return render(request, 'myhome/index.html', context)
    else:
        return render(request, 'myhome/index.html', {'properties': properties, 'logged_in': False})
    
def register(request):
    if request.method == 'POST':
        # Processi n the form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            return redirect('update_profile')

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

def verify(request, verification_token):
    try:
        # Find the user with the given verification token
        user = User.objects.get(is_email_verified=False, verification_token=verification_token)
        # Mark the user as verified
        user.is_email_verified = True
        user.save()
    except User.DoesNotExist:
        return HttpResponse('Failed to verify email')
    return redirect('update_profile')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        # If the user is  !authenticated, display an error message
        error_message = "Invalid username or password."
        return render(request, 'myhome/login.html', {'error_message': error_message, 'username': 'anonymous'})
    #so far so  good
    return render(request, 'myhome/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login')
    

def update_profile(request):
    try:
        profile = request.user
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        profile.first_name = request.POST.get('first_name', '')
        profile.last_name = request.POST.get('last_name', '')
        profile.account_type = request.POST.get('account_type', '')
        image = request.FILES.get('image')
        if image:
            profile.image = image
        profile.save()
        return redirect('profile')

    return render(request, 'myhome/update_profile.html', {'profile': profile})
    


def submit_property(request):
    if request.method == 'POST':
        form = SubmitPropertyForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return HttpResponse('Succcess') # Redirect to a success page after successful submission
    else:
        form = SubmitPropertyForm()

    return render(request, 'myhome/submit_property.html', {'form': form})
