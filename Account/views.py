# DRF
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import DefaultUser
from .serializers import UserDescSerializer, UserRegisterSerializer, UserLoginSerializer

""" 以下所有 API 未设置身份验证、权限验证 """

""" 用户详情 API 视图 """
class DefaultUserDetailView(generics.RetrieveAPIView):
    queryset = DefaultUser.objects.all()
    serializer_class = UserDescSerializer
    permission_classes = [IsAuthenticated]

""" 用户注册 API 视图：注册成功后返回用户信息和 token """
class RegisterApiView(generics.CreateAPIView):
    queryset = DefaultUser.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserDescSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

""" 用户登录 API 视图：登录成功后返回 token """
class LoginApiView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserDescSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class UpdateApiView(generics.UpdateAPIView):
    queryset = DefaultUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]

    # 使用 PUT 方法来更新用户信息
    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserDescSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

    def get_object(self):
        return self.request.user