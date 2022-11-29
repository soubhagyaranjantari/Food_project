from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    # from accounts import signals
    def ready(self):
        import accounts.signals
        # import vendor.signals