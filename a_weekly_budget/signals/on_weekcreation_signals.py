from django.dispatch import receiver
from django.db.models.signals import post_save
from a_weekly_budget.models import Week

@receiver(post_save, sender=Week)
def name_the_week(sender, instance, created, **kwargs):
    if created:
        new_week_position=instance.user.weeks.count()
        instance.name = f"Week {new_week_position}"
        instance.save()