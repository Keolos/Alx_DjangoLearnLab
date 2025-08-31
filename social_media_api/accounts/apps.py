from django.apps import AppConfig
from django.apps import AppConfig
from .apps import AccountsConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'


class AccountsConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from . import signals  # noqa
