from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants_count = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    country = CountryField(blank_label='(select country)', default='KE')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'profile_pics/', blank=True, default='profile_pics/default.jpg')
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, blank=True, default='1')

class Posts(models.Model):
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)    
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
