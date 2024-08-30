from rest_framework import serializers

from .models import Post
from Account.models import DefaultUser
from Account.serializers import UserHyperlinkSerializer

class PostSerializer(serializers.HyperlinkedModelSerializer):
    # author = UserHyperlinkSerializer()
    # author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'url', 'title', 'content', 'author', 'date_posted']
        extra_kwargs = {
            'author': {'view_name': 'post-detail', 'lookup_field': 'pk', 'read_only': True},
        }