from django.urls import path, include
# from . import views
from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView, UserPostListView, MyPostListView, PostCreate

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('Post/userposts/<str:username>/',
         UserPostListView.as_view(template_name='Post/user_posts.html'), name='user-posts'),

#     path('Post/topicposts/<str:topic>/',
#          TopicListView.as_view(template_name='Post/topic_posts.html'), name='topic-posts'),

    path('Post/list/<str:username>/',
         MyPostListView.as_view(template_name='Post/my_post.html'), name='my-posts'),
    path('Post/detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('Post/new/', PostCreateView.as_view(), name='post-create'),
    path('Post/<int:pk>/update/',
         PostUpdateView.as_view(template_name='Post/post_update.html'), name='post-update'),
    path('Post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('Post/create/', PostCreate, name='post-create'),
#     path('Post/topic/create/', views.TopicCreate, name='topic-create'),

#     path('about/', views.about, name='about'),
]
