from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class List(models.Model):
    #Alla atribut blir som sin egen rad
    title = models.CharField(max_length=75)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete= models.CASCADE)

