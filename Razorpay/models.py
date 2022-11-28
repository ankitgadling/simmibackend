from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class PeriodChoice(models.TextChoices):
    WEEKLY = "weekly", "Weekly"
    MONTHLY = "monthly", "Monthly"
    YEARLY = "yearly", "Yearly"


class StatusChoice(models.TextChoices):
    CREATED = "created", "Created"
    ACTIVE = "active", "Active"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"


class Transactions(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='payments')
    amount = models.CharField(max_length=25)
    is_paid = models.BooleanField(default=False)
    cause = models.CharField(max_length=50, default='Simmi Foundation')
    date = models.DateTimeField(auto_now=True)
    

class Subscription(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    plan_id = models.CharField(max_length=255)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='subscription')
    amount = models.CharField(max_length=25)
    cause = models.CharField(max_length=50, default='Simmi Foundation')
    period = models.CharField(max_length=10, choices=PeriodChoice.choices)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=StatusChoice.choices, default=StatusChoice.CREATED)
