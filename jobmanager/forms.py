from django import forms
from .models import Author, JobPost,Location

class JobPostForm(forms.ModelForm):
    city = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Enter the city'}))
    state = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Enter the state'}))
    country = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Enter the country'}))
    zipcode = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder':'Enter the zipcode'}))
    skills = forms.CharField(
        label='Skills',
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter skills separated by commas'}),
        required=False  # Not required because we will handle validation manually
    )

    class Meta:
        model = JobPost
        fields = ['title', 'description', 'skills', 'salary', 'application_deadline']

        widgets = {
                'title':forms.TextInput(attrs={'placeholder': 'Enter job title'}),
                'description': forms.TextInput(attrs={'placeholder': 'Enter description'}),
                'application_deadline':forms.DateInput(attrs={'placeholder': 'Give an application deadline'}),
                'salary':forms.NumberInput(attrs={'placeholder': 'Enter the salary'})
            }


class AuthorForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    class Meta:
        model = Author
        fields = ["name","company","designation"]

        widgets = {
            'company':forms.TextInput(attrs={'class':'form-control','placeholder':'Current Working Compnay'}),
            'designation':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your designation'})
        }