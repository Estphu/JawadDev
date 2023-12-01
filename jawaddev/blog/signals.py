from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image

from .models import Post

@receiver(pre_save, sender=Post)
def resize_image(sender, instance, **kwargs):
    if instance.thumbnail:
        img = Image.open(instance.thumbnail.path)

        # dimension
        new_width = 1200
        new_height = 600

        # Resize the image
        img.thumbnail((new_width, new_height))

        # saving the image to its path again
        img.save(instance.thumbnail.path)
