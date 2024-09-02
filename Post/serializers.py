from rest_framework import serializers

from .models import Post
from Account.models import DefaultUser
from Account.serializers import UserDescSerializer

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'url', 'title', 'author', 'content', 'date_posted']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

    def create(self, validated_data):
        post = Post.objects.create(
            title=validated_data['title'],
            content=validated_data['content'],
            author=validated_data['author']
        )
        return post

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        return super().update(instance, validated_data)