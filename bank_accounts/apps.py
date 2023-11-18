from django.apps import AppConfig
from django.core.signals import setting_changed


class BankAccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bank_accounts"

    def ready(self):
        from . import signals
