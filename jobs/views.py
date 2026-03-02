import os

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import JobApplicationForm
from .models import JobApplication, JobAttachment
from .services.gemini_client import GeminiAPIError, fetch_company_brief

ALLOWED_ATTACHMENT_EXTENSIONS = {'pdf', 'md', 'xls', 'xlsx', 'png', 'jpg', 'jpeg'}


def _create_attachments(job, files):
    for upload in files:
        extension = os.path.splitext(upload.name)[1].lower().lstrip('.')
        if extension not in ALLOWED_ATTACHMENT_EXTENSIONS:
            raise ValidationError(
                f"Unsupported file type: {upload.name}. Allowed: PDF, Markdown, Excel, PNG, JPG, JPEG"
            )
        JobAttachment.objects.create(job=job, file=upload)


def job_list(request):
    sort_by = request.GET.get('sort', 'created_at')

    if sort_by == 'application_deadline':
        jobs = JobApplication.objects.prefetch_related('attachments').all().order_by('application_deadline')
    elif sort_by == 'first_interview_date':
        jobs = JobApplication.objects.prefetch_related('attachments').all().order_by('first_interview_date')
    else:
        jobs = JobApplication.objects.prefetch_related('attachments').all().order_by('-created_at')

    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
        'current_sort': sort_by,
    })


def update_status(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        field = request.POST.get('field')
        status = request.POST.get('status')

        job = get_object_or_404(JobApplication, id=job_id)

        if field == 'application_status':
            job.application_status = status
        elif field == 'online_test_status':
            job.online_test_status = status
        elif field == 'first_interview_status':
            job.first_interview_status = status
        elif field == 'second_interview_status':
            job.second_interview_status = status
        elif field == 'notes_result':
            job.notes_result = status

        job.save()
        messages.success(request, f'{job.company_name} has been updated successfully.')

    return redirect('job_list')


def update_date(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        field = request.POST.get('field')
        date_value = request.POST.get('date_value') or None

        job = get_object_or_404(JobApplication, id=job_id)

        if field == 'application_deadline':
            job.application_deadline = date_value
        elif field == 'online_test_deadline':
            job.online_test_deadline = date_value
        elif field == 'first_interview_date':
            job.first_interview_date = date_value
        elif field == 'second_interview_date':
            job.second_interview_date = date_value

        job.save()
        messages.success(request, f"{job.company_name}'s date has been updated successfully.")

    return redirect('job_list')


def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            uploads = request.FILES.getlist('attachments')
            try:
                with transaction.atomic():
                    job = form.save()
                    _create_attachments(job, uploads)
            except ValidationError as exc:
                messages.error(request, str(exc))
            else:
                messages.success(request, 'New application added successfully!')
                return redirect('job_list')
        else:
            messages.error(request, f'form validation failed: {form.errors.as_text()}')
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/add_job.html', {'form': form})


def edit_job(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            uploads = request.FILES.getlist('attachments')
            try:
                with transaction.atomic():
                    form.save()
                    _create_attachments(job, uploads)
            except ValidationError as exc:
                messages.error(request, str(exc))
            else:
                messages.success(request, 'Application updated successfully!')
                return redirect('edit_job', job_id=job.id)
        else:
            messages.error(request, f'form validation failed: {form.errors.as_text()}')
    else:
        form = JobApplicationForm(instance=job)

    return render(request, 'jobs/edit_job.html', {
        'form': form,
        'job': job,
        'attachments': job.attachments.all(),
    })


@require_POST
def delete_attachment(request, job_id, attachment_id):
    job = get_object_or_404(JobApplication, id=job_id)
    attachment = get_object_or_404(JobAttachment, id=attachment_id, job=job)

    filename = attachment.filename
    attachment.delete()
    messages.success(request, f'{filename} deleted successfully.')

    return redirect('edit_job', job_id=job.id)


def delete_job(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id)
    if request.method == 'POST':
        company_name = job.company_name
        job.delete()
        messages.success(request, f'{company_name} has been deleted successfully.')
    return redirect('job_list')


@require_POST
def company_brief(request):
    """Return a Gemini-generated brief for the requested company."""
    company_name = request.POST.get('company_name', '').strip()
    if not company_name:
        return JsonResponse({'error': 'company_name is required.'}, status=400)

    try:
        brief = fetch_company_brief(company_name)
    except GeminiAPIError as exc:
        return JsonResponse({'error': str(exc)}, status=500)

    return JsonResponse({'company_name': company_name, 'brief': brief})
