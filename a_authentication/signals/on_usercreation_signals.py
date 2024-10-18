from django.dispatch import receiver
from django.db.models.signals import post_save
from a_authentication.models import CustomUser
from a_profile.models import Profile
from a_wallet.models import Wallet

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Wallet.objects.create(user=instance, name="Weekly wallet")