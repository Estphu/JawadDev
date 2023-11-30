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
    categories = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)