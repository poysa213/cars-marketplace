from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth import login


# from authentication.models import User
from rest_framework import serializers
from rest_framework import exceptions

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


# class LoginUserSerializer(serializers.Serializer):
#     username = serializers.CharField(allow_blank=True, required=False)
#     email = serializers.EmailField()
#     password = serializers.CharField(
#         style={'input_type': 'password'},
#         trim_whitespace=False
#     )

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=True, required=False)
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self,attrs):
        # get password, and username (or email)
        password = attrs.get("password")
        username = attrs.get("username")
        request = self.context.get('request')

        # set user to None
        user = None

        # check if a user exists with the email address or username provided
        if "@" in username:
            user = User.objects.filter(email__iexact=username).first()
        else:
            user = User.objects.filter(username__iexact=username).first()

        # raise an authentication failed error if a user with that username or email doesn't exist. 
        if user is None:
            raise exceptions.AuthenticationFailed(
                detail="Credentials does not exist!")

        else:
            # check if password matches
            if user.check_password(password):
                login(user=user, request=request)
                serializer = LoginUserSerializer(user).data
                return serializer

            # raise authentication failed error if it doesn't exist. 
            else:
                raise exceptions.AuthenticationFailed(
                    detail="Wrong password")



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