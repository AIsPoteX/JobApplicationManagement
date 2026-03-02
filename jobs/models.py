from django.core.validators import FileExtensionValidator
from django.db import models


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('---', '---'),
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    ]

    company_name = models.CharField(max_length=100, verbose_name="Company Name")

    application_deadline = models.DateField(null=True, blank=True, verbose_name="Application Deadline")
    online_test_deadline = models.DateField(null=True, blank=True, verbose_name="Online Test Deadline")
    first_interview_date = models.DateField(null=True, blank=True, verbose_name="First Interview Date")
    second_interview_date = models.DateField(null=True, blank=True, verbose_name="Second Interview Date")

    notes = models.TextField(max_length=500, blank=True, verbose_name="Memo")

    application_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="Application Status")
    online_test_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="Online Test Status")
    first_interview_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="First Interview Status")
    second_interview_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="Second Interview Status")
    notes_result = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="Memo Result")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"
        ordering = ['-created_at']


class JobAttachment(models.Model):
    ALLOWED_EXTENSIONS = ['pdf', 'md', 'xls', 'xlsx', 'png', 'jpg', 'jpeg']

    job = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name='attachments',
        verbose_name="Application",
    )
    file = models.FileField(
        upload_to='job_files/',
        validators=[FileExtensionValidator(ALLOWED_EXTENSIONS)],
        verbose_name="Attachment File",
        help_text="Allowed: PDF, Markdown, Excel, PNG, JPG, JPEG",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def filename(self):
        if self.file and getattr(self.file, "name", ""):
            return self.file.name.split("/")[-1]
        return ""

    def __str__(self):
        return self.filename or f"Attachment #{self.pk}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Attachment"
        verbose_name_plural = "Attachments"
