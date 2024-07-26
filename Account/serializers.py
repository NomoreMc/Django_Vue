from rest_framework import serializers
from .models import DefaultUser

class DefaultUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultUser
        fields = ['id', 'username', 'email', 'create_time', 'last_mod_time', 'source']