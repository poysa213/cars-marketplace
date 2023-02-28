
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.filters import SearchFilter





from .models import Service, ServiceProvider
from .serializers import ServiceProviderSerializer, ServiceSerializer, PostServiceProviderSerializer
from store.permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnlyProviderOwner
from .filters import ServiceFilter


class ServiceViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset  = Service.objects.all()
    serializer_class = ServiceSerializer
    filterset_fields = ['name']
    



class ServiceProviderViewSet(ModelViewSet):
    queryset  = ServiceProvider.objects.all()
    permission_classes = [IsOwnerOrAdminOrReadOnlyProviderOwner]
    filterset_class = ServiceFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service_provider = serializer.save()
        service_provider = ServiceProviderSerializer(serializer.data)
        return Response(service_provider.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save() 
        updated_serializer = self.get_serializer(updated_instance)
        return Response(ServiceProviderSerializer(ServiceProvider.objects.get(user_id=request.user.id)).data)

        


    def get_serializer_context(self):
        return {'user': self.request.user}
    
    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ServiceProviderSerializer
        else:
            return PostServiceProviderSerializer
        



