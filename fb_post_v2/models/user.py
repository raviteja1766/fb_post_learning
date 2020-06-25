from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100)
    profile_pic = models.TextField()
    # is_admin = models.BooleanField(default=False)
    # begin = models.DateField()
    # end = models.DateField()

    # def __str__(self):
    #     return f"{self.username} {self.begin} {self.end}"
