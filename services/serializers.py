from rest_framework import serializers

from .models import Service, ServiceProvider
from users.serializers import UserSerializer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name']

class ServiceProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    services = ServiceSerializer(many=True)
    class Meta:
        model = Service
        fields = ['id', 'user', 'services']

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        service_provider = ServiceProvider.objects.create(**validated_data)

        for service_data in services_data:
            service, _ =  Service.objects.get(**service_data)
            service_provider.services.add(service)
        return service_provider

