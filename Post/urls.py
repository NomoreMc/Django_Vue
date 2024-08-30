from django.urls import path

from .views import PostList, PostDetail

urlpatterns = [
    path('Post/listall/', PostList.as_view(), name='post-list'),
    path('Post/post-detail/<int:pk>', PostDetail.as_view(), name='post-detail'),
]
