from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=todos
        fields='__all__'

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mobile
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
    def create(self, validated_data):     # The create method define how fully fledged(developed) instances are created
                                            # or modify when calling serializer
                                            # method overiding
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=20)
    password=serializers.CharField(max_length=20)

class MixinSerializer(serializers.ModelSerializer):
    class Meta:
        model=MixinModel
        fields="__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeModel
        fields="__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=carModel
        fields="__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=MovieModel
        fields="__all__"


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonModel
        fields="__all__"


# #exam
# class RegSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields="__all__"
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
#
#
# class LogSerializer(serializers.Serializer):
#     username=serializers.CharField(max_length=20)
#     password=serializers.CharField(max_length=20)