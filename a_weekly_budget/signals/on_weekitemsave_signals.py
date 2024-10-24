from django.dispatch import receiver
from django.db.models.signals import post_save
from a_weekly_budget.models import WeekItemAssociation
from django.db.models import Sum

@receiver(post_save, sender=WeekItemAssociation)
def change_the_week_expenses_and_used_cash(sender, instance,**kwargs):
    totals = instance.week.week_item_association.aggregate(
    total_allocated=Sum('amount_allocated'),
    total_used=Sum('amount_used')
    )
    print(f"hello weekitem save {totals['total_allocated']}")
    instance.week.total_expenses=totals['total_allocated']
    instance.week.used_cash=totals['total_used']
    instance.week.save(update_fields=['total_expenses', 'used_cash'])