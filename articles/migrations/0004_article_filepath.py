# Generated by Django 3.1 on 2020-08-19 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200819_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='filePath',
            field=models.FilePathField(allow_files=False, allow_folders=True, blank=True),
        ),
    ]
