from rest_framework import serializers
# from rest_framework import viewsets
from .models import DefaultUser
from django.contrib.auth import authenticate

""" Post 列表中引用的嵌套序列化器 """
# class UserDescSerializer(serializers.ModelSerializer):
class UserDescSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk')
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk')
    class Meta:
        model = DefaultUser
        fields = ['id', 'username', 'email', 'url']
        # extra_kwargs = {
        #     'url': {'view_name': 'user-detail', 'lookup_field': 'pk'},
        # }


""" 用户注册以及更新时使用的序列化器 """
class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = DefaultUser
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # 验证邮箱是否已经存在
    def validate_email(self, value):
        if DefaultUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        user = DefaultUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        # instance.first_name = validated_data.get('first_name', instance.first_name)
        # instance.last_name = validated_data.get('last_name', instance.last_name)
        return super().update(instance, validated_data)
    


""" 用户登录使用的序列化器 """
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    """  """
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        data['user'] = user
        return user
    
# not using
class UserDetailSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    class Meta:
        model = DefaultUser
        fields = ['id', 'username', 'email', 'posts']

# for post hyperlink field
class UserHyperlinkSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='id')
    class Meta:
        model = DefaultUser
        fields = ['id', 'username', 'email', 'url']
        # extra_kwargs = {
        #     'url': {'view_name': 'user-detail'}
        # }