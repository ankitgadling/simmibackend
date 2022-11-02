from django.db import models
from django.contrib.auth.models import User
class LatestNews(models.Model):
    headline = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='latestnews', blank=True)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.headline
