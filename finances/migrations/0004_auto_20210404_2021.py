# Generated by Django 2.2.18 on 2021-04-04 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0003_auto_20210404_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer_details',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='customers.Client'),
        ),
    ]