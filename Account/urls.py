from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import DefaultUserDetailView

app_name = "Account"

urlpatterns = [
    re_path(r'^registration/$', views.RegisterView.as_view(), name='register', kwargs={'authentication_form': LoginForm}),


    re_path(r'^login/$', views.LoginView, name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='Account/logout.html'), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/<int:pk>/', DefaultUserDetailView.as_view(), name='user_detail'),
]