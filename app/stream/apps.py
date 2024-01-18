from django.apps import AppConfig


class StreamConfig(AppConfig):
    name = 'stream'

    def ready(self):
        import stream.signals
