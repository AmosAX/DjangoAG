from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    #här ska vi lägga till våra attribut
    #varje attribut är sitt eget fält I databasen
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    ##Obs att timezone kan defineras på olika sätt 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #on_delete, ifall våran användare bllir raderade tar vi bort alla deras listor

    ##magic method som 
    def __str__(self):
        return self.listname