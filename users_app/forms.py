from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import GuestCustomer

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomGuestRegisterForm(forms.ModelForm):
    class Meta:
        model = GuestCustomer
        fields = ['email']

