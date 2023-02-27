from rest_framework import serializers

from .models import Service, ServiceProvider
from users.serializers import UserSerializer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id']

    
class ServiceProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    services = ServiceSerializer(many=True)
    class Meta:
        model = Service
        fields = ['id', 'user', 'services']

class PostServiceProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    services_ids = serializers.ListField(child=serializers.IntegerField())
    class Meta:
        model = Service
        fields = ['id', 'user', 'services_ids']
    
    def get_services_id(self, obj):
        return [id for pk in obj]


    def create(self, validated_data):
        user = self.context.get('user')
        services_ids = validated_data.pop('services_ids', [])
        service_provider = ServiceProvider.objects.create(user=user, **validated_data)

        for service_id in services_ids:
            service =  Service.objects.get(id=service_id)
            print(service)
            print(service_id)
            if service is not None:
                service_provider.services.add(service)
        return service_provider

