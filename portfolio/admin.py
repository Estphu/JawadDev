from django.contrib import admin
from .models import Project, ProjectCategory, ProjectReview, ReviewFeature, ReviewLanguage, ReviewFramework, ReviewSoftware, ReviewInfrastructure, ReviewPackage

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(ProjectReview)
admin.site.register(ReviewFeature)
admin.site.register(ReviewLanguage)
admin.site.register(ReviewFramework)
admin.site.register(ReviewSoftware)
admin.site.register(ReviewInfrastructure)
admin.site.register(ReviewPackage)
