from django.db import models
from django.core.validators import FileExtensionValidator
import os

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('---', '---'),
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    ]
    
    # 公司名 - 必填
    company_name = models.CharField(max_length=100, verbose_name="Company Name")
    
    # 各个日期字段 - 可以为空
    application_deadline = models.DateField(null=True, blank=True ,verbose_name="Application Deadline")
    online_test_deadline = models.DateField(null=True, blank=True ,verbose_name="Online Test Deadline")
    first_interview_date = models.DateField(null=True, blank=True ,verbose_name="First Interview Date")
    second_interview_date = models.DateField(null=True, blank=True ,verbose_name="Second Interview Date")
    
    # 备注栏
    notes = models.TextField(max_length=500, blank=True , verbose_name="Memo")
    
    # PDF 文件上传
    pdf_file = models.FileField(
        upload_to='job_pdfs/',
        validators=[FileExtensionValidator(['pdf'])],
        blank=True,
        null=True,
        verbose_name="ES & Interview Notes",
        help_text="Only PDF"

    )
    
    @property
    def pdf_filename(self):
        if self.pdf_file and getattr(self.pdf_file, "name", ""):
            return os.path.basename(self.pdf_file.name)
        return ""
    

    # 各环节状态 - 除了公司名
    application_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="Application Status")
    online_test_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="Online Test Status")
    first_interview_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="First Interview Status")
    second_interview_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="Second Interview Status")
    notes_result = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="Memo Result")
    
    # 记录创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"
        ordering = ['-created_at']
