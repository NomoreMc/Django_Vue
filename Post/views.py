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
# post 创建视图
class PostApiCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

from .serializers import PostUpdateSerializer
from rest_framework import status
# post 更新视图
class PostApiUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def perform_update(self, serializer):
        serializer.save()


# post 删除视图
class PostApiDelete(APIView):
    def delete(self, request, pk):
        pass