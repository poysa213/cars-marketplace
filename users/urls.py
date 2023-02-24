from django.urls import path, include

from rest_framework import routers



from knox import views as knox_views
from .views import  LoginView, RegisterView, ProfileView, RegisterAdminView

router = routers.DefaultRouter()

router.register(r'profile', ProfileView)

urlpatterns = [
  path('register/',RegisterView.as_view(), name="create"),
  path('register/admin',RegisterAdminView.as_view(), name="create"),
  path('login/', LoginView.as_view(), name='knox_login'),
  path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
  path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
  path(r'', include(router.urls)),
 ] 
