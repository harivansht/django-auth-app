from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')


class PasswordChangeCustomForm(PasswordChangeForm):
    pass


class CustomPasswordResetForm(PasswordResetForm):
    pass


class CustomSetPasswordForm(SetPasswordForm):
    pass
