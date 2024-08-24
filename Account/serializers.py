from rest_framework import serializers
# from rest_framework import viewsets
from .models import DefaultUser
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultUser
        fields = ('id', 'username', 'password', 'email')
        # lookup_field = 'username'
        extra_kwargs = {
            'password': {'write_only': True}
            }

    def create(self, validated_data):
        user = DefaultUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
