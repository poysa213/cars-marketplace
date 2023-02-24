from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=255)

class ServiceProvider(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='user')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="providers" )