from django.db import models
import datetime

# Create your models here.
class Gallerytable(models.Model):
    options = (
        ("Education","Education"),
        ("Medical camps","Medical camps"),
        ("Livelihood","Livelihood"),
        ("Women empowerment","Women empowerment") 
   )
    title = models.CharField(max_length=50)
    admin = models.CharField(max_length=50,default="Test Admin")
    photo = models.ImageField(upload_to = "gallery")
    date = models.DateField(default=datetime.datetime.now())
    content = models.TextField()
    category = models.CharField(max_length=50,choices=options)
    #","livelihood",

    def __str__(self):
        return self.title