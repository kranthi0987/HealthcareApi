from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'apps.users.api.user'

    def ready(self):
        import apps.users.api.user.signals  # noqa
