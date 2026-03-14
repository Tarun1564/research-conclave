from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Evaluator, Evaluator, Uploads
import cloudinary.uploader
import os
@receiver(post_delete, sender=Uploads)
def remove_evaluation(sender, instance, **kwargs):
    for evaluator in Evaluator.objects.all():
        evaluator.papers.remove(instance)
@receiver(post_delete, sender=Uploads)
def delete_file_from_cloudinary(sender, instance, **kwargs):
    if instance.file:
        cloudinary.uploader.destroy(instance.file.public_id, resource_type="raw")