# Generated by Django 2.2.18 on 2021-04-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
