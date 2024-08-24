# Create your views here.

from rest_framework.views import APIView
from .serializer import PostSerializer
from rest_framework.response import Response
from .models import Post

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
    

class PostDetail(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass