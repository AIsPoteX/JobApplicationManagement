from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company_name', 'notes', 'pdf_file']
        widgets = {
            'notes': forms.Textarea(attrs={'maxlength': 100, 'placeholder': 'input...'}),
        }