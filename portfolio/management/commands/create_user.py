from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.utils import OperationalError
import os
from dotenv import load_dotenv
load_dotenv()

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            if not User.objects.filter(username="ogenna").exists():
                User.objects.create_superuser(username="ogenna", email="ogennaisrael@gmail.com", password=os.getenv("YourStrongPassword"))
        except OperationalError:
            self.stdout.write("Database not ready yet, skipping user creation.")
