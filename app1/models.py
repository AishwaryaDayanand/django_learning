from email.policy import default
from re import T
from statistics import mode
from django.db import models
import uuid

from users.models import Profile
# Create your models here.

class Project(models.Model):
    owner  = models.ForeignKey(Profile,null=True,blank=True ,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    demo_link = models.CharField(max_length=10000,null=True , blank=True)
    source_link = models.CharField(max_length=10000,null=True , blank=True)
    featured_imgs = models.ImageField(null=True , blank=True , default='default.jpg')
    tags = models.ManyToManyField("Tag" , blank=True)  #put Tag in quotes as Tag class is defined below this Project Class , if Tag is defined above this class can put Tag without quotes
    vote_total = models.IntegerField(default=0 , null=True , blank=True)
    vote_ratio= models.IntegerField(default=0 , null=True , blank=True)
    created  = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True,primary_key=True , editable=False)

    def __str__(self):
        return self.title
# 
class Review(models.Model):
    VOTE_TYPE = (
        ('up','up vote'),
        ('down','down vote')
    )

    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    body = models.TextField(null=True , blank=True)
    value =  models.CharField(max_length=200 , choices=VOTE_TYPE)  # drop down to choose values , tuple of tuples , first value of tuple is actual value stored , second value is displayed on screen
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True,primary_key=True , editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True,primary_key=True , editable=False)

    def __str__(self):
        return self.name
