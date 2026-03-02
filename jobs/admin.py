from django.contrib import admin

from .models import JobApplication, JobAttachment


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'application_deadline', 'first_interview_date', 'created_at')
    search_fields = ('company_name', 'notes')


@admin.register(JobAttachment)
class JobAttachmentAdmin(admin.ModelAdmin):
    list_display = ('filename', 'job', 'created_at')
    search_fields = ('file', 'job__company_name')
