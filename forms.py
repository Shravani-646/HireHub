from typing import Any
from django import forms 
from .models import JobApplication, JobPost,Skills

class JobApplicationForm(forms.ModelForm):
    skills = forms.CharField(help_text="Comma-seperated skills")

    class Meta:
        model = JobApplication
        fields = ["user","job_post","education","city","state","country","available_to_start","resume","skills"]

        widgets = {
                'education':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your highest degree','rows':3}),
                'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
                'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'}),
                'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your country'}),
            }


    def save(self,commit: bool = ...) -> Any:
        job_application = super().save(commit=False)
        skills_data = self.cleaned_data["skills"].split(",")
        skills = [Skills.objects.get_or_create(name=name.strip())[0] for name in skills_data]
        if commit:
            job_application.save()
            job_application.skills.set(skills)
        return job_application
        
