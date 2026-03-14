from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Evaluator, Evaluator, Uploads
import os

@receiver(post_delete, sender=Uploads)
def delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
@receiver(post_delete, sender=Uploads)
def remove_evaluation(sender, instance, **kwargs):
    for evaluator in Evaluator.objects.all():
        evaluator.papers.remove(instance)