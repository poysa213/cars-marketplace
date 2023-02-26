
from django.db import models

from users.models import User


class CarMarket(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class CarModel(models.Model):
    title = models.CharField(max_length=255)
    market = models.ForeignKey(CarMarket, on_delete=models.CASCADE, related_name="models")

    def __str__(self) -> str:
        return self.title



class Car(models.Model):

    CAR_STATE = (
    ("NEW", "New"),
    ("OLD", "Old"),
    )

    TRANSMISSION_TYPE = (
        ('AUTO', 'Auto'),
        ('MANUAL', 'Manual'),
        ('AUTOMANUAL', 'Auto Manual'),
    )

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars" )
    # title = models.CharField(max_length=255)
    seats = models.IntegerField(default=5, null=True)
    vitess = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    is_verify = models.BooleanField(default=False,)
    date = models.DateField(auto_now_add=True)
    state = models.CharField(choices=CAR_STATE, default='OLD', blank=True, max_length=255)
    market = models.ForeignKey(CarMarket, on_delete=models.CASCADE, related_name="cars", blank=True, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="cars", blank=True, null=True)
    transmission = models.CharField(max_length=12, choices=TRANSMISSION_TYPE, default='MANUAL', null=True )

    def __str__(self) -> str:
        return  str(self.market) + str(self.model) + str(self.seller)
    
class CarImage(models.Model):
    image = models.ImageField('store/images/cars', null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, related_name="images", blank=True)

class PartCategory(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name

class Part(models.Model):
    PART_STATE = (
    ("NEW", "New"),
    ("OLD", "Old"),
    )

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parts")
    category = models.ForeignKey(PartCategory, on_delete=models.CASCADE, related_name='parts')
    price = models.FloatField(null=True, blank=True)
    is_verify = models.BooleanField(default=False,)
    date = models.DateField(auto_now_add=True)
    state = models.CharField(choices=PART_STATE, default='NEW', blank=True, max_length=255)
    market = models.ForeignKey(CarMarket, on_delete=models.CASCADE, related_name="parts", blank=True, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="parts", blank=True, null=True)


    def __str__(self) -> str:
        return  str(self.market) + str(self.model) + str(self.seller)



class PartImage(models.Model):
    image = models.ImageField('store/images/parts',blank=True, null=True)
    part = models.ForeignKey(Part, on_delete=models.CASCADE, null= True, related_name="parts", blank=True)

