from django.apps import AppConfig
from django.contrib.auth.models import User


class MyauthConfig(AppConfig):
    name = 'myauth'

    def ready(self):
        try:
            User.objects.create_user('admincelero', 'admin@celero.com.br',
                                     'mypassword')
        except:
            pass
