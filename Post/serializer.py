from rest_framework import serializers

from .models import Post
from Account.models import DefaultUser


# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     author = serializers.StringRelatedField()
#     # author = serializers.PrimaryKeyRelatedField(queryset=DefaultUser.objects.all())
#     # author = serializers.SlugRelatedField(queryset=DefaultUser.objects.all(), slug_field='username')
#     # author = serializers.HyperlinkedRelatedField(
#     #     view_name='user-detail',
#     #     read_only=True,
#     #     lookup_field='username')
#     class Meta:
#         model = Post
#         # fields = ['title', 'content', 'author', 'date_posted']
#         fields = '__all__'
        
        
class PostSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    # author = serializers.PrimaryKeyRelatedField(queryset=DefaultUser.objects.all())
    # author = serializers.SlugRelatedField(queryset=DefaultUser.objects.all(), slug_field='username')
    # author = serializers.HyperlinkedRelatedField(
    #     view_name='user-detail',
    #     read_only=True,
    #     lookup_field='username')
    url = serializers.HyperlinkedIdentityField(view_name='post-detail')
    class Meta:
        model = Post
        # fields = ['title', 'content', 'author', 'date_posted']
        fields = '__all__'