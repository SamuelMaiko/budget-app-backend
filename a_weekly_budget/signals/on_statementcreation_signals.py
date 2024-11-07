from django.dispatch import receiver
from django.db.models.signals import post_save
from a_weekly_budget.models import Statement
from a_wallet.models import Wallet
from a_weekly_budget.models import WeekItemAssociation
from django.db.models import F, Sum
from a_expense_items.models import ExpenseItem

@receiver(post_save, sender=Statement)
def debit_the_weekitem_and_wallet_funds(sender, instance, created, **kwargs):
    if created:
        WeekItemAssociation.objects.filter(
            week=instance.week, 
            expense_item=instance.item_involved
            ).update(
                amount_used=F('amount_used')+instance.amount
                )
        
        item=ExpenseItem.objects.get(name="Other", user=instance.week.user)
        association=WeekItemAssociation.objects.get(expense_item=item, week=instance.week)
        
        totals = instance.week.week_item_association.exclude(id=association.id).aggregate(
        total_allocated=Sum('amount_allocated'),
        total_used=Sum('amount_used')+association.amount_used
        )
        print(f"hello statement {totals['total_allocated']}")
        instance.week.total_expenses = totals['total_allocated'] + association.amount_used if totals['total_allocated'] is not None else association.amount_used
        instance.week.used_cash=association.amount_used if totals['total_used'] is None else totals['total_used']
        instance.week.save(update_fields=['total_expenses', 'used_cash'])

        # reduce the extra funds (represented by Others item)
        # association.amount_allocated-=instance.amount
        # association.save()
        
        Wallet.objects.filter(
            name="Weekly wallet", 
            user=instance.week.user
            ).update(
                balance=F('balance')-instance.amount
                )
                
        
