# Generated by Django 2.2.19 on 2021-03-21 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0002_auto_20210319_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='team_member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]