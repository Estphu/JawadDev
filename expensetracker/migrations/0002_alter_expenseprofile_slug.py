# Generated by Django 5.0 on 2023-12-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensetracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseprofile',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]