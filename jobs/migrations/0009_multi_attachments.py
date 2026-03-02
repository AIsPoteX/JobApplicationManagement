from django.core.validators import FileExtensionValidator
from django.db import migrations, models
import django.db.models.deletion


def migrate_existing_pdf_to_attachments(apps, schema_editor):
    JobApplication = apps.get_model('jobs', 'JobApplication')
    JobAttachment = apps.get_model('jobs', 'JobAttachment')

    for job in JobApplication.objects.exclude(pdf_file='').exclude(pdf_file__isnull=True):
        JobAttachment.objects.create(
            job=job,
            file=job.pdf_file.name,
        )


class Migration(migrations.Migration):
    dependencies = [
        ('jobs', '0008_delete_jobattachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'file',
                    models.FileField(
                        help_text='Allowed: PDF, Markdown, Excel, PNG, JPG, JPEG',
                        upload_to='job_files/',
                        validators=[FileExtensionValidator(['pdf', 'md', 'xls', 'xlsx', 'png', 'jpg', 'jpeg']),],
                        verbose_name='Attachment File',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                (
                    'job',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='attachments',
                        to='jobs.jobapplication',
                        verbose_name='Application',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
                'ordering': ['-created_at'],
            },
        ),
        migrations.RunPython(migrate_existing_pdf_to_attachments, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='jobapplication',
            name='pdf_file',
        ),
    ]
