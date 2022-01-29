# Generated by Django 3.2.11 on 2022-01-29 08:09

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenge', '0011_auto_20220129_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='rules',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Rules related to submission (optional)', null=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
