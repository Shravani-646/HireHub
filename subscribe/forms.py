from typing import Any
from django import forms
from .models import Subscriber
from django.utils.translation import gettext_lazy as _

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["first_name","last_name","email","subscribe_type"]

        error_messages={
            'first_name':{
                'required':_("First name field is mandatory")
            }
        }
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'inp ml-2 ml-md-4 w-100 border p-2 m-1','placeholder':'Your first name'}),
            'last_name':forms.TextInput(attrs={'class':'inp ml-2 ml-md-4 w-100 border p-2 m-1','placeholder':'Your last name'}),
            'email':forms.EmailInput(attrs={'class':'inp ml-2 ml-md-4 w-100 border p-2 m-1','placeholder':'Your email'}),
            'subscribe_type': forms.Select(attrs={'class': 'inp ml-2 ml-md-4 w-100 border p-2 m-1'})
        }