# Generated by Django 2.2.18 on 2021-04-08 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0017_remove_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='inventory',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
