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
        # 获取对应的 user 实例
        user = self.get_object()
        # 获取序列化器实例，传入 user 实例和 request.data，后者将用于更新 user 实例
        serializer = self.get_serializer(user, data=request.data)
        # 验证数据是否合法
        serializer.is_valid(raise_exception=True)
        # 调用 perform_update，内部会调用序列化器的 update 方法进行实际的更新操作
        self.perform_update(serializer)
        # 为 user 生成新的 token
        refresh = RefreshToken.for_user(user)
        # 返回更新后的 user 信息和 token
        return Response({
            'user': UserDescSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

    # 重写 get_object 方法，返回当前请求的用户实例
    def get_object(self):
        return self.request.user