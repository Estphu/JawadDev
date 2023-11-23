from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class ProjectCategory(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

class Project(models.Model):
    slug = models.SlugField(max_length=120, editable=False)
    title = models.CharField(max_length=60)
    thumbnail = models.ImageField(upload_to='portfolio/thumbnails/')
    btn_title = models.CharField(max_length=60)
    desc = models.TextField(max_length=500)
    link = models.URLField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(ProjectCategory)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        img = Image.open(self.thumbnail.path) # Open image

        # resize image
        if img.height > 800 or img.width > 600:
            output_size = (800, 600)
            img.thumbnail(output_size) # Resize image
            img.save(self.thumbnail) # Save it again and override the larger image