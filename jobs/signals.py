from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from .models import JobAttachment


@receiver(post_delete, sender=JobAttachment)
def delete_attachment_file_on_delete(sender, instance, **kwargs):
    """Delete physical file when attachment record is deleted."""
    if instance.file:
        instance.file.delete(save=False)


@receiver(pre_save, sender=JobAttachment)
def delete_old_attachment_file_on_change(sender, instance, **kwargs):
    """Delete previous physical file when attachment file is replaced."""
    if not instance.pk:
        return

    try:
        old = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    old_file = old.file
    new_file = instance.file
    if old_file and old_file != new_file:
        old_file.delete(save=False)
