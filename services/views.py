
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS


from .models import Service, ServiceProvider
from .serializers import ServiceProviderSerializer, ServiceSerializer, PostServiceProviderSerializer
from store.permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly, IsOwnerOrAdminOrReadOnlyProviderOwner



class ServiceViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset  = Service.objects.all()
    serializer_class = ServiceSerializer
    

class ServiceProviderViewSet(ModelViewSet):
    queryset  = ServiceProvider.objects.all()
    serializer_class = PostServiceProviderSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnlyProviderOwner]


    def get_serializer_context(self):
        return {'user': self.request.user}
    
    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ServiceProviderSerializer
        else:
            return PostServiceProviderSerializer


