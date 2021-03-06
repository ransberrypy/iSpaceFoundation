# Generated by Django 2.2.18 on 2021-04-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20210322_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(blank=True, max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
