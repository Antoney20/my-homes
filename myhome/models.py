from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username