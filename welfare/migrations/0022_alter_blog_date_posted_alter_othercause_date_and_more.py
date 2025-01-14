# Generated by Django 4.1.2 on 2023-03-29 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0021_blog_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateField(default=datetime.date(2023, 3, 29)),
        ),
        migrations.AlterField(
            model_name='othercause',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 29)),
        ),
        migrations.AlterField(
            model_name='story',
            name='issue_on',
            field=models.DateField(default=datetime.date(2023, 3, 29)),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 29)),
        ),
    ]
