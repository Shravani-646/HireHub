from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from .models import User
from django import forms

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User 
        fields = ["username","first_name","last_name","email","password1","password2"]

        widgets = {
                'username':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a username'}),
                'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
                'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter the password again'})