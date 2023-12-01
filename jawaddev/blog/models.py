from collections.abc import Iterable
from typing import Any
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class PostCategory(models.Model):
    slug = models.SlugField(max_length=128, null=True, editable=False)
    title = models.CharField(max_length=64)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["title"]        

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, null=True)
    title = models.CharField(max_length=128)
    content = RichTextField()
    thumbnail = models.ImageField(upload_to='blog/thumbnails/')
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    word_count = models.PositiveIntegerField()
    reading_time = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(PostCategory)

    def __str__(self):
        return f"{self.author.username} - {self.title}"
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def publish(self):
        self.published_date = timezone.now()
        self.is_published = True
        self.save()  

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["updated_date"]    



