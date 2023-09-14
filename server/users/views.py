from django.contrib.auth import login
from django.contrib.auth  import get_user_model


from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework import generics,status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from .serializers import LoginUserSerializer, UserSerializer, RegisterSerializer, RegisterAdminSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import IsOwnerOrAdminOrReadOnlyProfileOwner


User = get_user_model()


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            _, token = AuthToken.objects.create(user)
            return Response({
                "user": UserSerializer(user,context=self.get_serializer_context()).data,
                "token":  token
            })
        return Response(serializer.data, status=status.HTTP_401_BAD_REQUEST)


class LoginView(KnoxLoginView, AuthTokenSerializer):
    serializer_class = LoginUserSerializer
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user":  UserSerializer(user).data,
            "token": AuthToken.objects.create(user)[1]
        })


class ProfileView(GenericViewSet, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnlyProfileOwner]
    queryset = UserProfile.objects.select_related('user').all()
    lookup_field = 'id'

   

    def get_queryset(self):
        if self.action == "list":
            return UserProfile.objects.filter(user_id=self.request.user.id)
        else:
            return super().get_queryset()

            #  return UserProfile.objects.filter(user_id=self.request.user.id)

     # def get_permissions(self):
    #     if self.action == 'list':
    #         return [IsAdminUser()]
    #     if self.action == 'get' or 'update' or 'retreive':
    #         return [IsOwnerOrAdminOrReadOnlyProfileOwner()]
    
    # def get_queryset(self, request):
    #     return UserProfile.objects.filter(user_id=self.request.user.id)

class RegisterAdminView(generics.CreateAPIView):
    serializer_class = RegisterAdminSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
