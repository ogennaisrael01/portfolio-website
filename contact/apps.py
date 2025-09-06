import os
from django.apps import AppConfig
from django.contrib.auth import get_user_model


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'

    def ready(self):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username=os.environ.get("DJANGO_SUPERUSER_USERNAME"),
                email=os.environ.get("DJANGO_SUPERUSER_EMAIL"),
                password=os.environ.get("DJANGO_SUPERUSER_PASSWORD")
            )
