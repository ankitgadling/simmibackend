# Generated by Django 4.1.2 on 2022-10-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('immediate_supervisor', models.CharField(max_length=50)),
                ('salary_range', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=50000)),
            ],
        ),
    ]