# Generated by Django 4.2.7 on 2023-11-29 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_remove_project_categories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectCategory',
        ),
    ]
