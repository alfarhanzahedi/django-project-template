from django.contrib.auth.models import AbstractUser
from django.db import models

# User model to be used throughout the project.
# Refer to: https://wsvincent.com/django-custom-user-model-tutorial/.
class User(AbstractUser):
    pass
    # Add additional fields (say, age or gender) here.

    def __str__(self):
        return self.username
