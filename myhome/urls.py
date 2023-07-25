from django.urls import path
from .import views


urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path('verify/<str:verification_token>/', views.verify, name='verify'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('submitproperty/', views.submit_property, name='submit_property'),
]


