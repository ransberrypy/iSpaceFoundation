# Generated by Django 2.2.18 on 2021-04-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0008_auto_20210404_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
