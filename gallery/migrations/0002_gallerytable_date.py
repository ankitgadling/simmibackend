# Generated by Django 4.1.2 on 2022-11-09 23:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerytable',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 9, 23, 15, 29, 48554)),
        ),
    ]