# Generated by Django 2.2.19 on 2021-03-20 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_space_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='space',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
