# Create your views here.

from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from .models import Post

class PostApiList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

class PostApiDetail(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

from rest_framework import generics
from .serializers import PostCreateSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
# post 创建视图
class PostApiCreate(generics.CreateAPIView):
    # 使用 knox token auth 进行身份验证
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from .serializers import PostUpdateSerializer
from rest_framework import status
# post 更新视图
class PostApiUpdate(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer

    def put(self, request, *args, **kwargs):
        # 获取对象
        instance = self.get_object()
        # 创建序列化器
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        # 验证数据
        serializer.is_valid(raise_exception=True)
        # 执行数据更新操作
        self.perform_update(serializer)
        # 返回更新后的数据以及状态码
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()


# post 删除视图
class PostApiDelete(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    queryset = Post.objects.all()

    def delete(self, request, pk):
        instance = self.get_object()

        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()