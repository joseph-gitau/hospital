# import the standard Django Model
# from built-in library
from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

# Create your models here.
# declare a new model with a name"employee"
class Employee(models.Model):
    # fields of the model
    eid = models.AutoField(primary_key=True,serialize = False,verbose_name ='ID')
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    epassword = models.CharField(max_length=120, blank=True, null=True)
    econtact = models.CharField(max_length=15)
    edob = models.DateField(blank=True, null=True)# If no date is selected then Django  saves blank field value.

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk': self.pk})
    #objects = models.Manager()
    class Meta:
        db_table = "employee"
        ordering = ['eid',]#sorts the records ascending using 'eid' field

class UserProfileDoc(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=25,null=True)
    dob = models.DateField(blank=True,null=True)  # If no date is selected then Django saves blank field value.
    city = models.CharField(max_length=25,null=True)
    contactno = models.CharField(max_length=25,null=True)
    portfolio_site = models.URLField(blank=True,null=True)
    image = models.ImageField(null=True,upload_to='images/', default = 'images/None/no-img.jpg',blank=True)



