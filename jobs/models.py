from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('---', '---'),
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    ]
    
    # 公司名 - 必填
    company_name = models.CharField(max_length=100, verbose_name="公司名")
    
    # 各个日期字段 - 可以为空
    application_deadline = models.DateField(null=True, blank=True, verbose_name="投递截至日期")
    online_test_deadline = models.DateField(null=True, blank=True, verbose_name="网测截至日期")
    first_interview_date = models.DateField(null=True, blank=True, verbose_name="一面日期")
    second_interview_date = models.DateField(null=True, blank=True, verbose_name="二面日期")
    
    # 备注栏
    notes = models.TextField(max_length=100, blank=True, verbose_name="备注")
    
    # 各环节状态 - 除了公司名
    application_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="投递状态")
    online_test_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="网测状态")
    first_interview_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="一面状态")
    second_interview_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="二面状态")
    notes_result = models.CharField(max_length=10, choices=STATUS_CHOICES, default='---', verbose_name="备注结果")
    
    # 记录创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name = "求职申请"
        verbose_name_plural = "求职申请"
        ordering = ['-created_at']
