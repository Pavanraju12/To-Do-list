from django import forms

from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
    # pass
    email=forms.EmailField()