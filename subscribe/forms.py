from typing import Any
from django import forms
from .models import Subscriber
from django.utils.translation import gettext_lazy as _

# class SubscriberForm(forms.Form):
#     first_name = forms.CharField(max_length=255)
#     last_name = forms.CharField(max_length=255)
#     email = forms.EmailField(max_length=255)

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('email')
        
#         if email and Subscriber.objects.filter(email=email).exists():
#             raise forms.ValidationError("This email is already used to subscribe, try with another mail")
        
#         return cleaned_data

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["first_name","last_name","email","subscribe_type"]

        error_messages={
            'first_name':{
                'required':_("First name field is mandatory")
            }
        }