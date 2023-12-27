from django.db import models

# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=120)
    img_url = models.URLField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    step = models.CharField()
    instruction = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.cake.name