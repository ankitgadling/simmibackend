# Generated by Django 4.1.2 on 2022-11-04 08:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='upi_tran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('paas', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(8)])),
            ],
        ),
    ]
