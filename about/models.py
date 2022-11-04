from turtle import position
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class About(models.Model):

    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=80)
    desc = models.TextField()

class Founders(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=80)
    img = models.ImageField(upload_to = "about/Founders/")
    desc = models.TextField()

class Advisory_board(models.Model):
    
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=80)
    img = models.ImageField(upload_to = "about/Board Commitee Members/")
    desc = models.TextField()

class Senior_management_committee(models.Model):
    
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=80)
    img = models.ImageField(upload_to = "about/Senior Commitee Members/")
    desc = models.TextField()

class Senior_technical_committee(models.Model):
    
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=80)
    img = models.ImageField(upload_to = "about/Senior tech Commitee Members/")
    desc = models.TextField()

class Team(models.Model):

    name = models.CharField(max_length=50)
    position = models.CharField(max_length=80)
    img = models.ImageField(upload_to = "about/Team Members/")


class Our_initiatives(models.Model):
    options = (
        ("Education","Education"),
        ("Medical camps","Medical camps"),
        ("Livelihood","Livelihood"),
        ("Healthcare","Healthcare"),
        ("Women empowerment","Women empowerment") 
   )
    title_category = models.CharField(max_length=50,choices=options)
    photo = models.ImageField(upload_to = "about/initiatives/")
    content = models.TextField()

class Our_campaigns(models.Model):
    options = (
        ("Education","Education"),
        ("Medical camps","Medical camps"),
        ("Livelihood","Livelihood"),
        ("Healthcare","Healthcare"),
        ("Women empowerment","Women empowerment") 
   )   
    title_category = models.CharField(max_length=50,choices=options)
    photo = models.ImageField(upload_to = "about/campaigns/")
    content = models.TextField()


