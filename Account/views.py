from django.shortcuts import render, redirect
# from django.contrib.sites.shortcuts import get_current_site

# Create your views here.

# 重构User模块
from django.conf import settings
from django.views.generic import FormView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
# 用于验证User的基类，用这个form来接收username和password
# from django.contrib.auth.forms import AuthenticationForm
# from django.views.decorators.debug import sensitive_post_parameters
# from django.http import HttpResponseRedirect
# from django.utils.http import url_has_allowed_host_and_scheme

# 用于验证用户
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, smart_str
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from datetime import datetime, timedelta

from .models import DefaultUser

# DRF
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import DefaultUser
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserLoginSerializer

class DefaultUserDetailView(generics.RetrieveAPIView):
    queryset = DefaultUser.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerializer
    
    # permission_classes = [IsAuthenticated]

# register api view
class RegisterApiView(generics.CreateAPIView):
    queryset = DefaultUser.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


# login api view
class LoginApiView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

from rest_framework import viewsets


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = DefaultUser.objects.all()
#     serializer_class = UserSerializer
