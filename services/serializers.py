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
    # services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)

    class Meta:
        model = ServiceProvider
        fields = ['id', 'user', 'services']

class PostServiceProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    services_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    class Meta:
        model = ServiceProvider
        fields = ['id', 'user', 'services_ids']


    def create(self, validated_data):
        user = self.context.get('user')
        if user.is_authenticated:
            services_ids = validated_data.pop('services_ids', [])
            service_provider = ServiceProvider.objects.create(user=user, **validated_data)

            for service_id in services_ids:
                service =  Service.objects.get(id=service_id)
                if service is not None:
                    service_provider.services.add(service)
            return service_provider
        raise serializers.ValidationError({'message': "You must login!"})
        
    
    def update(self, instance, validated_data):
        services_ids = validated_data.pop('services_ids', [])
        # services = Service.objects.filter(id__in=services_ids)
        if services_ids is not None:
            instance.services.set(services_ids)
        return instance



