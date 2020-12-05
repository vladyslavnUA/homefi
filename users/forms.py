from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True),
    email = forms.EmailField(max_length=50, required=True),

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')