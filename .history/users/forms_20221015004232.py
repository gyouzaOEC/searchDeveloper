from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = user
        