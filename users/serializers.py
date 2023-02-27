from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth import login


# from authentication.models import User
from rest_framework import serializers
from rest_framework import exceptions

from .models import UserProfile


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')



class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['user', 'phone_number', 'image', 'address', 'birth_date']

        
 
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=True, required=False)
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
    



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        password_data = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password_data)
        user.save()
        return user
    

class RegisterAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password_data = validated_data.pop('password')
        user = User.objects.create_superuser(**validated_data)
        user.set_password(password_data)
        user.save()
        return user