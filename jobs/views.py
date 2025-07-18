from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import JobApplication

def job_list(request):
    # 获取排序参数
    sort_by = request.GET.get('sort', 'created_at')
    
    # 验证排序参数
    if sort_by == 'application_deadline':
        # 按投递截至日期排序，空值排在最后
        jobs = JobApplication.objects.all().order_by('application_deadline')
    elif sort_by == 'first_interview_date':
        # 按一面日期排序，空值排在最后
        jobs = JobApplication.objects.all().order_by('first_interview_date')
    else:
        # 默认按创建时间降序排序
        jobs = JobApplication.objects.all().order_by('-created_at')
    
    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
        'current_sort': sort_by
    })

def update_status(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        field = request.POST.get('field')
        status = request.POST.get('status')
        
        job = get_object_or_404(JobApplication, id=job_id)
        
        # 更新对应的状态字段
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
        messages.success(request, f'{job.company_name} 的状态已更新')
    
    return redirect('job_list')

def update_date(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        field = request.POST.get('field')
        date_value = request.POST.get('date_value') or None
        
        job = get_object_or_404(JobApplication, id=job_id)
        
        # 更新对应的日期字段
        if field == 'application_deadline':
            job.application_deadline = date_value
        elif field == 'online_test_deadline':
            job.online_test_deadline = date_value
        elif field == 'first_interview_date':
            job.first_interview_date = date_value
        elif field == 'second_interview_date':
            job.second_interview_date = date_value
        
        job.save()
        messages.success(request, f'{job.company_name} 的日期已更新')
    
    return redirect('job_list')

def add_job(request):
    if request.method == 'POST':
        # 获取表单数据
        company_name = request.POST.get('company_name')
        notes = request.POST.get('notes', '')
        
        # 创建新记录
        if company_name:
            JobApplication.objects.create(
                company_name=company_name,
                notes=notes
            )
            messages.success(request, '成功添加新的求职记录！')
        else:
            messages.error(request, '公司名不能为空！')
            
        return redirect('job_list')
    
    return render(request, 'jobs/add_job.html')

def edit_job(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id)
    
    if request.method == 'POST':
        # 只更新公司名和备注
        job.company_name = request.POST.get('company_name', job.company_name)
        job.notes = request.POST.get('notes', '')
        
        job.save()
        messages.success(request, '求职记录更新成功！')
        return redirect('job_list')
    
    return render(request, 'jobs/edit_job.html', {'job': job})

def delete_job(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id)
    if request.method == 'POST':
        company_name = job.company_name
        job.delete()
        messages.success(request, f'已删除 {company_name} 的求职记录！')
    return redirect('job_list')
