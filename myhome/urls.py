from django.urls import path
from .import views
from myhome import views as myhomev

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", myhomev.logout_user, name="logout"),
    
    path('verify/<str:verification_token>/', views.verify, name='verify'),
    #profile
    path('update_profile/', views.update_profile, name='update_profile'),
    path('submitproperty/', views.submit_property, name='submitproperty'),
    path('property/<int:SubmitProperty_id>/', views.property_details, name='property_details'),

    path('agent/<int:agent_id>/', views.agent_details, name='agent'),
    path('agents/', views.agents, name='all-agents'),
]


