from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.contrib.auth.hashers import make_password

import uuid



class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    objects = UserManager()

    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
