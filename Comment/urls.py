from django.urls import path

from . import views

app_name = "comments"
urlpatterns = [
    path('Post/<int:post_id>/postcomment', views.CommentPostView.as_view(), name='post-comment'),
]