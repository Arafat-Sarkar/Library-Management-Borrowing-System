from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(AbstractUser):
    pass
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    penalty_points = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    