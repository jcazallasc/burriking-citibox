from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Django command to create my super user
    """

    def handle(self, *args, **options):
        _email = "jcazallasc@gmail.com"

        if not User.objects.filter(email=_email).exists():
            User.objects.create_superuser(_email, _email, "cazallas")
