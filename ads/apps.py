from django.apps import AppConfig


class AdsConfig(AppConfig):
    name = 'ads'

    def ready(self):
        import ads.signals
