# Generated by Django 3.2.11 on 2022-01-29 06:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0008_auto_20220128_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='timeline',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
