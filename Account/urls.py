from django.urls import path

from .views import DefaultUserDetailView, RegisterApiView, LoginApiView, UpdateApiView

# 缺一个 logout view
urlpatterns = [
    path('Account/api/user/register/', RegisterApiView.as_view(), name='user-register'),
    # path('Account/api/user/login/', LoginApiView.as_view(), name='user-login'),
    path('Account/api/user/update/', UpdateApiView.as_view(), name='user-update'),
    path('Account/api/user/<int:pk>/', DefaultUserDetailView.as_view(), name='user-detail'),
]