from django import forms

from .models import JobApplication


class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultiFileField(forms.FileField):
    def clean(self, data, initial=None):
        single_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_clean(item, initial) for item in data if item]
        if not data:
            return []
        return [single_clean(data, initial)]


class JobApplicationForm(forms.ModelForm):
    attachments = MultiFileField(
        required=False,
        widget=MultiFileInput(attrs={
            'multiple': True,
            'accept': '.pdf,.md,.xls,.xlsx,.png,.jpg,.jpeg',
        }),
        help_text='Allowed: PDF, Markdown, Excel, PNG, JPG, JPEG',
        label='Attachments',
    )

    class Meta:
        model = JobApplication
        fields = ['company_name', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'maxlength': 500, 'placeholder': 'input...'}),
        }
