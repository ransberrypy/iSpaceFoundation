# Generated by Django 2.2.19 on 2021-03-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('telephone', models.CharField(max_length=120)),
                ('details', models.TextField()),
                ('called_back', models.BooleanField(default=False)),
                ('feedback_details', models.TextField(blank=True)),
            ],
        ),
    ]