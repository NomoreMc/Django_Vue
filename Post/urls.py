from django.urls import path

from .views import PostApiList, PostApiDetail, PostApiCreate, PostApiUpdate, PostApiDelete

urlpatterns = [
    path('Post/api/post/list/', PostApiList.as_view(), name='post-list'),
    path('Post/api/post/detail/<int:pk>', PostApiDetail.as_view(), name='post-detail'),
    path('Post/api/post/create/', PostApiCreate.as_view(), name='post-create'),
    path('Post/api/post/update/<int:pk>', PostApiUpdate.as_view(), name='post-update'),
    path('Post/api/post/delete/<int:pk>', PostApiDelete.as_view(), name='post-delete'),
]
