from rest_framework_nested import routers


from .views import ServiceViewSet, ServiceProviderViewSet

router = routers.DefaultRouter()

router.register('services', ServiceViewSet)
router.register('providers', ServiceProviderViewSet)
# services_router = routers.NestedDefaultRouter(router, '', lookup='car')

# services_router.register('providers', ServiceProviderViewSet)


urlpatterns = router.urls 