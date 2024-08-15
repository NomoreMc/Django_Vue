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
# from .forms import LoginForm, CaptchaLoginForm, UserUpdateForm, ProfileUpdateForm

# class RegisterView(FormView):
#     form_class = RegisterForm
#     template_name = 'Account/registration_page.html'
#     url = '/login/'

#     @method_decorator(csrf_protect)
#     def dispatch(self, *args, **kwargs):
#         return super(RegisterView, self).dispatch(*args, **kwargs)

#     def form_valid(self, form):
#         if form.is_valid():
#             user = form.save(commit=False)
#             # 此处应当先设置为False，之后在通过邮箱验证后才设置为True，验证有效性
#             user.is_active = False
#             # 标定用户创建途径，通过页面注册的用户，后续会有三方的形式注册
#             user.source = 'Register'
#             # 设置用户的最后登录时间
#             user.last_login = datetime.now()
#             user.save(True)

#             # current_site 是当前网站的域名
#             # current_site = get_current_site(self.request)
#             current_site = settings.SITE_DOMAIN
#             # 生成邮件主题
#             mail_subject = 'Activate your account.'
#             # 生成邮件内容
#             message = render_to_string('Account/activate_email.html', {
#                 'user': user,
#                 'domain': current_site,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': default_token_generator.make_token(user),
#             })
#             # 生成 EmailMessage 实例
#             email = EmailMessage(
#                 mail_subject, message, to=[form.cleaned_data.get('email')]
#             )
#             # 发送邮件
#             email.send()

#             return render(self.request, 'Account/auth_email_send_done.html')
#             # return HttpResponseRedirect('/login/')
#         else:
#             return self.render_to_response({
#                 'form': form
#             })

def Activate(request, uid, token):
    try:
        uid = smart_str(urlsafe_base64_decode(uid))
        user = DefaultUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, DefaultUser.DoesNotExist):
        user = None
    
    # 检查用户是否存在
    if user is not None:
        # 获取 user 实例的创建时间
        token_created_at = datetime.fromtimestamp(int(user.date_joined.timestamp()))
        # 查看当前时间
        now = datetime.now()
        # 判断 token 是否在有效期内
        token_age = now - token_created_at

        # 如果 token 超过 15 分钟，则视为过期
        if token_age > timedelta(minutes=15):
            # 删除用户
            user.delete()
            return render(request, 'Account/auth_email_confirm_expired.html')
        
        # 如果 token 有效，则激活用户
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'Account/auth_email_confirm_done.html')
        else:
            # 否则删除用户
            user.delete()
            return render(request, 'Account/auth_email_confirm_fail.html')
    else:
        return render(request, 'Account/auth_email_confirm_fail.html')

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
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

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

    # def perform_create(self, serializer):
    #     user = serializer.save()
    #     user.set_password(user.password)
    #     user.save()
    #     # current_site = get_current_site(self.request)
    #     current_site = settings.SITE_DOMAIN
    #     mail_subject = 'Activate your account.'
    #     message = render_to_string('Account/activate_email.html', {
    #         'user': user,
    #         'domain': current_site,
    #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #         'token': default_token_generator.make_token(user),
    #     })
    #     email = EmailMessage(
    #         mail_subject, message, to=[user.email]
    #     )
    #     email.send()

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
    

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
