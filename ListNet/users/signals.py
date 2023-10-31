from django.db.models.signals import post_save
from django.dispatch import receiver
#SIGNALS SAKERNA VI BEHÖVER

#Ta in en user från django ramverket
from django.contrib.auth.models import User
#ta profiles som är vår egna
from .models import Profile

#Skapa en "lyssnare"

@receiver(post_save, sender = User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)
    

@receiver(post_save, sender = User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
