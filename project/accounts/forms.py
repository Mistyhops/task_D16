from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class BaseRegisterForm(UserCreationForm):
    username = forms.CharField(label='Никнейм')
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
