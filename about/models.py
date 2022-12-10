from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# class About(models.Model):

#     title = models.CharField(max_length=50)
#     sub_title = models.CharField(max_length=80)
#     desc = models.TextField()
#     sub_desc=models.TextField()

# class Founders(models.Model):
#     name = models.CharField(max_length=50)
#     position = models.CharField(max_length=80)
#     img = models.ImageField(upload_to = "about/Founders/")
#     desc = models.TextField()
#     instaid=models.URLField(default="https://www.instagram.com/")
#     tweetid=models.URLField(default="https://twitter.com/")
#     fbid=models.URLField(default="https://www.facebook.com/Meta/")

# class Advisory_board(models.Model):
    
#     name = models.CharField(max_length=50)
#     position = models.CharField(max_length=80)
#     img = models.ImageField(upload_to = "about/Board Commitee Members/")
#     desc = models.TextField()
#     instaid=models.URLField(default="https://www.instagram.com/")
#     tweetid=models.URLField(default="https://twitter.com/")
#     fbid=models.URLField(default="https://www.facebook.com/Meta/")

# class Senior_management_committee(models.Model):
    
#     name = models.CharField(max_length=50)
#     position = models.CharField(max_length=80)
#     img = models.ImageField(upload_to = "about/Senior Commitee Members/")
#     desc = models.TextField()
#     instaid=models.URLField(default="https://www.instagram.com/")
#     tweetid=models.URLField(default="https://twitter.com/")
#     fbid=models.URLField(default="https://www.facebook.com/Meta/")

# class Senior_technical_committee(models.Model):
    
#     name = models.CharField(max_length=50)
#     position = models.CharField(max_length=80)
#     img = models.ImageField(upload_to = "about/Senior tech Commitee Members/")
#     desc = models.TextField()
#     instaid=models.URLField(default="https://www.instagram.com/")
#     tweetid=models.URLField(default="https://twitter.com/")
#     fbid=models.URLField(default="https://www.facebook.com/Meta/")

# class Team(models.Model):

#     name = models.CharField(max_length=50)
#     position = models.CharField(max_length=80)
#     img = models.ImageField(upload_to = "about/Team Members/")


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
    name=models.CharField(max_length=25) 
    position=models.CharField(max_length=100) 
    insta_id=models.URLField()
    meta_id=models.URLField()
    tweet_id=models.URLField()
    img=models.ImageField() 