from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views

# from . import views
# from .forms import LoginForm

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import DefaultUserDetailView, RegisterApiView, LoginApiView, UpdateApiView

app_name = "Account"

# 缺一个 logout view
urlpatterns = [
    path('api/user/register/', RegisterApiView.as_view(), name='register'),
    path('api/user/login/', LoginApiView.as_view(), name='login'),
    path('api/user/update/', UpdateApiView.as_view(), name='update'),
    path('api/user/<int:pk>/', DefaultUserDetailView.as_view(), name='user-detail'),
    # re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='Account/logout.html'), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]