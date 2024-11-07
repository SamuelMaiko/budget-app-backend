from django.dispatch import receiver
from django.db.models.signals import post_save
from a_authentication.models import CustomUser
from a_profile.models import Profile
from a_wallet.models import Wallet
from a_expense_items.models import ExpenseItem
from a_weekly_budget.models import Week
from datetime import datetime, timedelta

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Wallet.objects.create(user=instance, name="Weekly wallet")
        ExpenseItem.objects.create(name="Other", user=instance)
        Week.objects.create(
            name="gjhg",
            user=instance,
            start_date=datetime.today(),
            end_date=datetime.today() + timedelta(days=7)
        )
