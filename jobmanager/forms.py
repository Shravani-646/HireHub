from django import forms
from .models import Author, JobPost,Location

class JobPostForm(forms.ModelForm):
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    zipcode = forms.CharField(max_length=10)
    skills = forms.CharField(
        label='Skills',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter skills separated by commas'}),
        required=False  # Not required because we will handle validation manually
    )

    class Meta:
        model = JobPost
        fields = ['title', 'description', 'skills', 'salary', 'application_deadline']


class AuthorForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    class Meta:
        model = Author
        fields = ["name","company","designation"]