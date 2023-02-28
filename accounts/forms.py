from django import forms
from .models import Account


class RegisterationForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Enter Password'
  }))
  class Meta:
    model = Account
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']