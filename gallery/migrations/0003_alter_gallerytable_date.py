# Generated by Django 4.1.2 on 2022-11-10 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_gallerytable_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerytable',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 10, 16, 51, 57, 170912)),
        ),
    ]