from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail_url = models.URLField(max_length=200)
    link_url = models.URLField(max_length=200)
    title = models.CharField(max_length=60, unique=True)
    tag = models.CharField(max_length=60, null=True)
    author = models.CharField(max_length=60)
    desc = models.TextField(max_length=500)
    extra = models.CharField(max_length=100)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()
        self.is_published = True
        self.save() 

class BookKeyPoint(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    point = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.book.title} - ({self.point})"  
