from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="ogenna").exists():
            User.objects.create_superuser(
                username="ogenna",
                email="ogennaisrael@gamil.com",
                password=os.getenv("YourStrongPassword")
            )
            self.stdout.write(self.style.SUCCESS("Superuser created!"))
        else:
            self.stdout.write("Superuser already exists.")
