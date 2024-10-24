from django.dispatch import receiver
from django.db.models.signals import post_save
from a_weekly_budget.models import Statement
from a_wallet.models import Wallet
from a_weekly_budget.models import WeekItemAssociation
from django.db.models import F, Sum

@receiver(post_save, sender=Statement)
def debit_the_weekitem_and_wallet_funds(sender, instance, created, **kwargs):
    if created:
        WeekItemAssociation.objects.filter(
            week=instance.week, 
            expense_item=instance.item_involved
            ).update(
                amount_used=F('amount_used')+instance.amount
                )
        
        totals = instance.week.week_item_association.aggregate(
        total_allocated=Sum('amount_allocated'),
        total_used=Sum('amount_used')
        )
        print(f"hello statement {totals['total_allocated']}")
        instance.week.total_expenses=totals['total_allocated']
        instance.week.used_cash=totals['total_used']
        instance.week.save(update_fields=['total_expenses', 'used_cash'])
        
        Wallet.objects.filter(
            name="Weekly wallet", 
            user=instance.week.user
            ).update(
                balance=F('balance')-instance.amount
                )
                
        
