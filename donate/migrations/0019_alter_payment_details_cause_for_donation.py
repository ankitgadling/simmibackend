# Generated by Django 4.1.2 on 2022-12-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0018_alter_payment_details_cause_for_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_details',
            name='cause_for_donation',
            field=models.CharField(choices=[('HealthCare', 'HealthCare'), ('Other', 'Other'), ('Livlihood', 'Livlihood'), ('Women Empowerment', 'Women Empowerment'), ('Education', 'Education')], max_length=100),
        ),
    ]