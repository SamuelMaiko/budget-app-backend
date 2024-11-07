from django.apps import AppConfig


class AWeeklyBudgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_weekly_budget'

    def ready(self):
        from .signals import on_weekcreation_signals, on_statementcreation_signals, on_weekitemsave_signals
