from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

QUESTIONS = (
    ('What was the name of your first pet?', 'What was the name of your first pet?'),
    ('In which city or town were you born?', 'In which city or town were you born?'),
    ('What is the title of your favorite book or movie?', 'What is the title of your favorite book or movie?'),
    ('What is the name of the city where you attended your first concert?', 'What is the name of the city where you attended your first concert?'),
    ('Who is your favorite author or film director?', 'Who is your favorite author or film director?')
)

TYPE = (
    ('Positive', 'Positive'),
    ('Negative', 'Negative'),
)

# Create your models here.
class ExpenseProfile(models.Model):
    slug = models.SlugField(editable=False)
    username = models.CharField(max_length=60, unique=True)
    question = models.CharField(choices=QUESTIONS)
    answer = models.CharField(max_length=128)
    income = models.FloatField()
    expense = models.FloatField(default=0)
    balance = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("expensetracker:expense_tracker_view", kwargs={"slug": self.slug})
        

class ExpenseTracker(models.Model):
    profile = models.ForeignKey(ExpenseProfile,on_delete=models.CASCADE)
    expense_text = models.CharField(max_length=50)
    amount = models.FloatField(null=True)
    expense_type = models.CharField(max_length=50,choices=TYPE)

    def __str__(self):
        return self.expense_text