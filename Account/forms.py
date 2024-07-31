# User模块重构，创建新的模块
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError
from django import forms
from captcha.fields import CaptchaField

from .models import DefaultUser, Profile

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.widgets.TextInput(
            attrs={'placeholder': "username", "class": "form-control"})
        self.fields['email'].widget = forms.widgets.EmailInput(
            attrs={'placeholder': "email", "class": "form-control"})
        self.fields['password1'].widget = forms.widgets.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control"})
        self.fields['password2'].widget = forms.widgets.PasswordInput(
            attrs={'placeholder': "repeat password", "class": "form-control"})

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("该邮箱已经存在.")
        return email

    class Meta:
        model = get_user_model()
        fields = ("username", "email")

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(
            attrs={'placeholder': "username", "class": "form-control"})
        self.fields['password'].widget = forms.widgets.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control"})

# 带有验证码的登录表单，继承自 LoginForm，仅多了 captcha 字段
class CaptchaLoginForm(LoginForm):
    captcha = CaptchaField(label='验证码')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = DefaultUser
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']