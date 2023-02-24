from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.contrib.auth.hashers import make_password

import uuid



class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    objects = UserManager()
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.email



    



class Wilaya(models.Model):
    name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Daira(models.Model):
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name="dairas")
    name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
class Address(models.Model):
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    daira = models.ForeignKey(Daira, on_delete=models.CASCADE)
    longitude = models.FileField(blank=True, null=True)
    latitude = models.FileField(blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True) 
    birth_date = models.DateField(blank=True, null=True)