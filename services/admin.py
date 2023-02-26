from django.contrib import admin


from .models import Service, ServiceProvider


admin.site.register(Service)
admin.site.register(ServiceProvider)