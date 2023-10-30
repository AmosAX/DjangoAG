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


from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
    #on delete avgör återigen vad som ska ske om våran använder försvinner
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Default kommer vara template bilden alla våra ny användare får, Upload_to är ditt alla våra profil bilder blir
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #Vi vill kunna skriva ut user username, 
    #Försöker vi göra det direkt kommer den läsa det som ett objekt och ge oss något som inte är läsbart för människor
    def __str__(self):
        return f'{self.user.username} Profile'
    
    #Vi behöver importa från pillow

    def save(self):
    super().save()
    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)

