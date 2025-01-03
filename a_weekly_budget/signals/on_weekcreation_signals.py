from django.dispatch import receiver
from django.db.models.signals import post_save
from a_weekly_budget.models import Week, WeekItemAssociation
from a_wallet.models import Wallet
from a_expense_items.models import ExpenseItem

@receiver(post_save, sender=Week)
def name_the_week(sender, instance, created, **kwargs):
    if created:
        new_week_position=instance.user.weeks.count()
        instance.name = f"Week {new_week_position}"
        instance.save()

        # adding "Other" item to a week after creation
        item=ExpenseItem.objects.get(name="Other", user=instance.user)
        wallet=Wallet.objects.get(name="Weekly wallet", user=instance.user)
        WeekItemAssociation.objects.create(expense_item=item, week=instance, amount_allocated=wallet.balance)

    # item=ExpenseItem.objects.get(name="Other", user=instance.user)
    # association=WeekItemAssociation.objects.get(expense_item=item, week=instance)
    # wallet=Wallet.objects.get(name="Weekly wallet", user=instance.user)
    # association.amount_allocated=(wallet.balance+instance.used_cash) - instance.total_expenses
    # association.save()


        
