
from django.db import models

from users.models import User


class CarMarket(models.Model):
    title = models.CharField(max_length=255)
    


class CarModel(models.Model):
    title = models.CharField(max_length=255)
    market = models.ForeignKey(CarMarket, on_delete=models.CASCADE,)

class CarImage(models.Model):
    image = models.ImageField(null=True, blank=True)

class Car(models.Model):

    CAR_STATE = (
    ("NEW", "New"),
    ("OLD", "Old"),
    )

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars" )
    title = models.CharField(max_length=255)
    seats = models.IntegerField(default=5, null=True)
    vitess = models.IntegerField(null=True, blank=True)
    images = models.ForeignKey(CarImage, on_delete=models.CASCADE)
    price = models.FloatField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    is_verify = models.BooleanField(default=False,)
    date = models.DateField(auto_now_add=True)
    state = models.CharField(choices=CAR_STATE, default='OLD', blank=True, max_length=255)
    market = models.ForeignKey(CarMarket, on_delete=models.CASCADE, related_name="cars", blank=True, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="cars", blank=True, null=True)

class PartImage(models.Model):
    image = models.ImageField(blank=True)
class PartCategory(models.Model):
    name = models.CharField(max_length=255)

class Part(models.Model):
    PART_STATE = (
    ("NEW", "New"),
    ("OLD", "Old"),
    )

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parts")
    category = models.ForeignKey(PartCategory, on_delete=models.CASCADE, related_name='parts')
    images = models.ForeignKey(PartImage, on_delete=models.CASCADE, related_name='parts')
    price = models.FloatField(null=True, blank=True)
    is_verify = models.BooleanField(default=False,)
    date = models.DateField(auto_now_add=True)
    state = models.CharField(choices=PART_STATE, default='NEW', blank=True, max_length=255)
    market = models.ForeignKey(CarMarket, on_delete=models.CASCADE, related_name="parts", blank=True, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="parts", blank=True, null=True)



