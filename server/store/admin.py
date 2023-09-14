from django.contrib import admin

from .models import Car, CarImage, CarMarket, CarModel, PartImage, PartCategory, Part

admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(CarMarket)
admin.site.register(CarModel)
admin.site.register(PartImage)
admin.site.register(PartCategory)
admin.site.register(Part)
