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
from django.shortcuts import render, get_object_or_404
from .models import SubmitProperty
# Create your views here.

@login_required
def index(request):
    properties = SubmitProperty.objects.all()
    user = request.user
    name='index page'
    
    context = {
        'properties': properties,
        'user': user,
        'name': name,   
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
            alert_message = "Email already registered. Please login."
            return render(request, 'myhome/login.html', {'alert_message': alert_message})

        
        
                # Create a new user object and saving him to the db
        user = User(username=username, email=email, password=password)
        verification_token = user.generate_verification_token()
        user.save()

        # Send the verification email to the user
        subject = 'Email Verification'
        message = f'Hi {username}Click the link to verify your email: {request.build_absolute_uri("/")}/app/verify/{user.verification_token}/'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        return redirect('login')
        
        return redirect('success')
    
    return render(request, 'myhome/register.html')

def verify(request, verification_token):
    try:
        # Find the user with the given verification token
        user = User.objects.get(is_email_verified=False, verification_token=verification_token)
        
        # Mark the user as verified
        user.is_email_verified = True
        user.save()
        return render(request, 'myhome/index.html') 
    except User.DoesNotExist:
        return HttpResponse('Please register')
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
@login_required
def property_details(request, SubmitProperty_id):
    propertys= get_object_or_404(SubmitProperty, pk=SubmitProperty_id)
    user = request.user
    name= 'Property details'
        # Filter related properties
    property_type = propertys.property_type
    related_properties = SubmitProperty.objects.filter(property_type=property_type).exclude(pk=SubmitProperty_id)
    agent = propertys.user.username
    agent_id = propertys.user.id
    
    
    context = {
        'property': propertys,
        'name': name,
        'user': user,
        'agent': agent,
        'agent_id': agent_id,
        'logged_in': True, 
        'related_properties': related_properties,
    }
    if user.is_authenticated:
        return render(request, 'myhome/property_detail.html', context)
    else:
        return render(request, 'myhome/property_detail.html', {'properties': properties, 'logged_in': False})
    
    
#agents
def agent(request, user_id):
    agent = get_object_or_404(User, id=user_id)
    properties = SubmitProperty.objects.filter(user=agent)
    context = {'agent': agent, 'properties': properties}
    return render(request, 'myhome/agent.html', context)