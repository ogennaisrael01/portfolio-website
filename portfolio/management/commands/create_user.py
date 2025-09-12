from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Create default superuser if not exists"

    def handle(self, *args, **kwargs):
        username = "ogenna"
        email = "ogenna@example.com"
        password = "password123"  # Change this after first login!

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created with password '{password}'"))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists"))

