from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class About(models.Model):

    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=80)
    desc = models.TextField()
    sub_desc=models.TextField()


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


class commonAboutTable(models.Model):
    options = (
        ("Founder","Founder"),
        ("Co-Founder","Co-Founder"),
        ("Advisory Board Committee","Advisory Board Committee"),
        ("Senior Management Committe","Senior Management Committe"),
        ("Senior Technical Committee","Senior Technical Committee") ,
        ("Executive Team","Executive Team")
   )  
    name = models.CharField(max_length=50)
    position = models.CharField(choices = options, max_length=80)
    team_name=models.CharField(max_length=50,null=True)
    img = models.ImageField(upload_to = "about/")
    desc = models.TextField(null=True)
    instaid=models.URLField(null=True)
    tweetid=models.URLField(null=True)
    fbid=models.URLField(null=True)