from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 30:
            raise ValidationError('Длина превышает 30 символов')
        return name


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Пароль'}))

