# Generated by Django 5.0 on 2023-12-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakepicker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instruction',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
