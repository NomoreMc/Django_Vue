from rest_framework import serializers

from .models import Post
from Account.models import DefaultUser


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'date_posted']