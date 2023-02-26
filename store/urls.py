from django.urls import path, include


from rest_framework_nested import routers

from .views import CarMarketViewSet, CarViewSet, CarModelViewSet, CarImageViewSet

router = routers.DefaultRouter()

router.register('markets', CarMarketViewSet)
router.register('models', CarModelViewSet)
router.register('cars', CarViewSet, basename='car')

cars_router = routers.NestedDefaultRouter(router, 'cars', lookup="car")
cars_router.register('images', CarImageViewSet, basename="image")




urlpatterns = router.urls +cars_router.urls


