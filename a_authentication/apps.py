from django.apps import AppConfig


class AAuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_authentication'

    def ready(self):
        from .signals import on_usercreation_signals
