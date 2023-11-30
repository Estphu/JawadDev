from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image

from .models import Project

@receiver(pre_save, sender=Project)
def resize_image(sender, instance, **kwargs):
    if instance.thumbnail:
        img = Image.open(instance.image.path)

        # dimension
        new_width = 600
        new_height = 800

        # Resize the image
        img.thumbnail((new_width, new_height))

        # saving the image to its path again
        img.save(instance.thumbnail.path)
