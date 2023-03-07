from django.urls import path, include


from rest_framework_nested import routers

from .views import CarMarketViewSet, CarViewSet, CarModelViewSet, CarImageViewSet, PartViewSet , PartImageViewSet, PartImageViewSet, PartCategoryViewSet

router = routers.DefaultRouter()

router.register('markets', CarMarketViewSet)
router.register('models', CarModelViewSet)
router.register('cars', CarViewSet, basename='car')
router.register('parts', PartViewSet, basename='part')
router.register('partcategory', PartCategoryViewSet, basename='partcategory')

cars_router = routers.NestedSimpleRouter(router, 'cars', lookup="car")
cars_router.register('images', CarImageViewSet, basename="image")

parts_router = routers.NestedSimpleRouter(router, 'parts', lookup="part")
parts_router.register('images', PartImageViewSet, basename="image")


urlpatterns = router.urls + cars_router.urls + parts_router.urls


