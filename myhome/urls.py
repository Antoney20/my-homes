from django.urls import path
from .import views
from myhome import views as myhomev

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", myhomev.logout_user, name="logout"),
    path('verify/<str:verification_token>/', views.verify, name='verify'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('submitproperty/', views.submit_property, name='submitproperty'),
]


