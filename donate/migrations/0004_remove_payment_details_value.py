# Generated by Django 4.1.2 on 2022-10-18 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0003_payment_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_details',
            name='value',
        ),
    ]