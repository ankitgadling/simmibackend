from django.db import models
from account.models import SimmiUser

class LatestNews(models.Model):
    headline = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(SimmiUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='latestnews', blank=True)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.headline
