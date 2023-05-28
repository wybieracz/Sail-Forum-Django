from django.apps import AppConfig

class BoardsConfig(AppConfig):
    name = 'boards'
    verbose_name = 'Kategorie'

default_app_config = 'boards.apps.BoardsConfig'