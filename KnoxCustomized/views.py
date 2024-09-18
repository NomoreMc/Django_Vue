from rest_framework import generics
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = AuthTokenSerializer  # 使用 DRF 自带的认证序列化器

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # 调用 is_valid 时会调用序列化器的 validate 方法，validate 方法会调用 authenticate 方法进行用户验证
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        instance, token = AuthToken.objects.create(user)
        # 创建并返回 Knox 令牌
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
            },
            "expiry": instance.expiry,
            "token": token
        })