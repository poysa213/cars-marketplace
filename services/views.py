
from rest_framework.viewsets import ModelViewSet


from .models import Service, ServiceProvider
from .serializers import ServiceProviderSerializer, ServiceSerializer
from store.permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly



class ServiceViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset  = Service.objects.all()
    serializer_class = ServiceSerializer
    

class ServiceProviderViewSet(ModelViewSet):
    queryset  = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]


