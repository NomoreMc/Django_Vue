from rest_framework import generics
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = AuthTokenSerializer  # 使用 DRF 自带的认证序列化器

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        # 创建并返回 Knox 令牌
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
            },
            "token": AuthToken.objects.create(user)[1]
        })