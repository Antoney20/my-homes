from django.db import models



# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    account_type = models.CharField(max_length=50, choices=[('Free', 'Free'), ('Premium', 'Premium')], default='Free')
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class SubmitProperty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    specific_description = models.TextField()
    content = models.TextField()
    property_type = models.CharField(choices=(
        ('Hostel', 'Hostel'),
        ('Apartment', 'Apartment'),
        ('Flat', 'Flat'),
        ('Building', 'Building'),
        ('House', 'House'),
        ('Villa', 'Villa'),
        ('Office', 'Office'),
    ), max_length=50)
    selling_type = models.CharField(choices=(
        ('Rent', 'Rent'),
        ('Sale', 'Sale'),
    ), max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    total_rooms = models.PositiveIntegerField()
    area_size = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    image1 = models.ImageField(upload_to='property_images/')
    image2 = models.ImageField(upload_to='property_images/')
    image3 = models.ImageField(upload_to='property_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='property_images/', blank=True, null=True)
    status = models.CharField(choices=(
        ('Available', 'Available'),
        ('Sold Out', 'Sold Out'),
    ), max_length=50)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
