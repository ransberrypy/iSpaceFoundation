# Generated by Django 2.2.18 on 2021-04-04 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0012_reconciliation'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_match',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Reconciliation',
        ),
    ]
