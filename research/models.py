from django.db import models

# Create your models here.


class ResearchTable(models.Model):
    title = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    how_we_helped = models.TextField()
    year = models.IntegerField()
    article_link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="research")
    