from django.apps import AppConfig


class VendorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor'
    # # from vendor import signals
    # def ready(self):
    #     import vendor.signals
