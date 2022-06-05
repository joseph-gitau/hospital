from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=25,null=True)
    dob = models.DateField(blank=True,null=True)  # If no date is selected then Django saves blank field value.
    city = models.CharField(max_length=25,null=True)
    contactno = models.CharField(max_length=25,null=True)
    portfolio_site = models.URLField(blank=True,null=True)
    image = models.ImageField(null=True,upload_to='images/', default = 'images/None/no-img.jpg',blank=True)
    class Meta:
        permissions = [
            ("save data", "Can save data into database"),
            ("read data", "Can only read data"),
        ]

''' class Profile(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField(max_length=200, default='Home')
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=True)
 '''