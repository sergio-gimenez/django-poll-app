from django import forms
from django.contrib.auth.forms import UserCreationForm  # Default form from django
from django.contrib.auth.models import User  # Default user model from django


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field to the form

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
