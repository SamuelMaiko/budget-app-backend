from django.dispatch import receiver
from django.db.models.signals import post_save
from a_weekly_budget.models import WeekItemAssociation
from django.db.models import Sum
from a_expense_items.models import ExpenseItem
from a_wallet.models import Wallet

@receiver(post_save, sender=WeekItemAssociation)
def change_the_week_expenses_and_used_cash(sender, instance,**kwargs):
    if instance.expense_item.name !="Other":
        item=ExpenseItem.objects.get(name="Other", user=instance.week.user)
        association=WeekItemAssociation.objects.get(expense_item=item, week=instance.week)


        totals = instance.week.week_item_association.exclude(id=association.id).aggregate(
        total_allocated=Sum('amount_allocated'),
        total_used=Sum('amount_used')
        )
        print(f"allocated {totals['total_allocated']}")
        instance.week.total_expenses=totals['total_allocated']+association.amount_used
        instance.week.used_cash=totals['total_used']+association.amount_used
        instance.week.save(update_fields=['total_expenses', 'used_cash'])

        association=WeekItemAssociation.objects.get(expense_item=item, week=instance.week)
        wallet=Wallet.objects.get(name="Weekly wallet", user=instance.week.user)
        # print() 
        # association.amount_allocated=wallet.balance + instance.week.used_cash - totals['total_allocated']-instance.week.used_cash
        association.amount_allocated=wallet.balance - totals['total_allocated'] + association.amount_used
        print("saved")
        association.save()
    else:
        print("found nothing 😂")

    # association.amount_allocated=(wallet.balance+instance.used_cash) - instance.total_expenses
    # association.save()