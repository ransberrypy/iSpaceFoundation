# Generated by Django 2.2.19 on 2021-03-19 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0002_auto_20210319_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(blank=True, help_text='Name of Organization', max_length=120)),
                ('title', models.CharField(blank=True, help_text='Name of Event', max_length=120)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('duration', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, help_text='What its about, Chair person')),
                ('number_of_attendants', models.IntegerField(blank=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
                ('program', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='services.Program')),
            ],
        ),
    ]