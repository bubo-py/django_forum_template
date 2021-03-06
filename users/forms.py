from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('user_avatar', )
