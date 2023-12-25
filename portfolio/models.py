from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

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
    featured = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ReviewLanguage(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title 

class ReviewFramework(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title 

class ReviewSoftware(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title 

class ReviewInfrastructure(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title 

class ReviewPackage(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title 

class ProjectReview(models.Model):
    slug = models.SlugField(max_length=120, editable=False, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    sub_title = models.CharField(max_length=200)
    type = models.CharField(max_length=60)
    web_name = models.CharField(max_length=60)
    web_url = models.URLField()
    github_url = models.URLField()
    introduction = models.TextField()
    Objectives = models.TextField()
    approach = models.TextField()
    evaluation = models.TextField()
    languages = models.ManyToManyField(ReviewLanguage)
    frameworks = models.ManyToManyField(ReviewFramework)
    softwares = models.ManyToManyField(ReviewSoftware)
    infrastructures = models.ManyToManyField(ReviewInfrastructure)
    packages = models.ManyToManyField(ReviewPackage)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("portfolio:review_detail", kwargs={"slug": self.slug})
    
    def formatted_introduction(self):
        return '<p>' + '</p><p>'.join(self.introduction.split('\n')) + '</p>'
    
    def formatted_objectives(self):
        return '<p>' + '</p><p>'.join(self.Objectives.split('\n')) + '</p>'
    
    def formatted_approach(self):
        return '<p>' + '</p><p>'.join(self.approach.split('\n')) + '</p>'
    
    def formatted_evaluation(self):
        return '<p>' + '</p><p>'.join(self.evaluation.split('\n')) + '</p>'
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ReviewFeature(models.Model):
    project_review = models.ForeignKey(ProjectReview, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.project_review.title

