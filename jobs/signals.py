from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from .models import JobApplication


@receiver(post_delete, sender=JobApplication)
def delete_pdf_on_delete(sender, instance, **kwargs):
    """删除记录时顺便删除关联的 PDF 文件。"""
    if instance.pdf_file:
        instance.pdf_file.delete(save=False)


@receiver(pre_save, sender=JobApplication)
def delete_old_pdf_on_change(sender, instance, **kwargs):
    """替换 PDF 时删除旧文件，避免堆积孤儿文件。"""
    if not instance.pk:
        return
    try:
        old = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    new_file = instance.pdf_file
    old_file = old.pdf_file
    if old_file and old_file != new_file:
        old_file.delete(save=False)
