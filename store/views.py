


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from .models import CarMarket, CarImage, CarModel, Car
from .serializers import CarMarketSerializer, CarModelSerializer, CarSerializer, CarImageSerializer, PostCarSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly, IsOwnerOrAdminOrReadOnlyImageOwner

class CarMarketViewSet(ModelViewSet):
    queryset = CarMarket.objects.all()
    serializer_class = CarMarketSerializer
    permission_classes = [IsAdminOrReadOnly,]


class CarModelViewSet(ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [IsAdminOrReadOnly,]

    


class CarImageViewSet(ModelViewSet):
    serializer_class = CarImageSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnlyImageOwner]
 

    def get_serializer_context(self):
        return {'car_id': self.kwargs.get('car_pk')}

    def get_queryset(self):
        return CarImage.objects.filter(car_id=self.kwargs.get('car_pk'))
    

class CarViewSet(ModelViewSet):
    queryset = Car.objects.prefetch_related("images").all()
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CarSerializer
        else:
            return PostCarSerializer
            

    def get_serializer_context(self):
        return {'user': self.request.user}
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, files=request.FILES)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #    serializer.save(seller=self.request.user)
