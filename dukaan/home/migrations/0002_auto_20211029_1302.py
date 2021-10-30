# Generated by Django 3.2.8 on 2021-10-29 07:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_id',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='margin',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
