# Generated by Django 4.1.2 on 2022-12-18 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0014_alter_payment_details_cause_for_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_details',
            name='cause_for_donation',
            field=models.CharField(choices=[('Other', 'Other'), ('Livlihood', 'Livlihood'), ('Education', 'Education'), ('Women Empowerment', 'Women Empowerment'), ('HealthCare', 'HealthCare')], max_length=100),
        ),
    ]
