from django.contrib import admin

from .models import User,SubmitProperty,Profile
# Register your models here.

admin.site.register(User)

admin.site.register(SubmitProperty)
admin.site.register(Profile)