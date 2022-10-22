from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    profile_pics = models.ImageField(upload_to="profile/images", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return  reverse('profile', kwargs={"id":self.id})