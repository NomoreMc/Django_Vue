from django.urls import path, include

from .views import PostList

urlpatterns = [
    path('Post/listall/', PostList.as_view(), name='post-list'),
]
