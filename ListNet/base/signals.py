from django.db.models.signals import post_save  # Importera signalen för "post_save".
from django.contrib.auth.models import User  # Importera Django's inbyggda User-modell.
from django.dispatch import receiver  # Importera reciver.
from .models import Profile  # Importera vår egena Profile-modell.

# Skapa en signalmottagare för "post_save" som lyssnar på när en ny User skapas.


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:  # Kolla om en ny User just har skapats.
        # Om det är en ny User, skapa en tillhörande Profile.
        Profile.objects.create(user=instance)

# Skapa en signalmottagare som lyssnar på när en User uppdateras.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # När en User uppdateras, spara också den tillhörande Profile.
    instance.profile.save()