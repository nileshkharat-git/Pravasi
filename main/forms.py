from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import accounts

class RegiForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Email")
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Username')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label='Confirm password')
    class Meta:
        model=accounts
        fields=['email','username','password1','password2']


