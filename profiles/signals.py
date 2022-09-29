from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile
# from .utils import generate_ref_code

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
      