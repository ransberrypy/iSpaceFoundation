# Generated by Django 2.2.19 on 2021-03-19 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
        ('events', '0001_initial'),
        ('customers', '0002_auto_20210319_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='event',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spaceuser',
            name='booking',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='bookings.Booking'),
            preserve_default=False,
        ),
    ]