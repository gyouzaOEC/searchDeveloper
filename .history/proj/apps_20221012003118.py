from django.apps import AppConfig


class ProjConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'proj'

    def ready(self):
        import users.signals