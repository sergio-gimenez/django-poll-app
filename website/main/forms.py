from django import forms
from django.contrib.auth.forms import UserCreationForm  # Default form from django
from django.contrib.auth.models import User  # Default user model from django

from .models import Post


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


class PostForm(forms.ModelForm):
    # This will create an instance of a form, pass the instance to a template. The template will display the form for
    # us and then we can add more things such as the author.
    class Meta:
        model = Post
        fields = ('title', 'description')
