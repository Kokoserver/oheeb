# Generated by Django 3.0.6 on 2020-05-26 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200526_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 26, 9, 1, 44, 290419)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 26, 9, 1, 44, 290419)),
        ),
    ]