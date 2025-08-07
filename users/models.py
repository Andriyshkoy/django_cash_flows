from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Extends Django's built-in user model without modifications."""
