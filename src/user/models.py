from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profilepic.jpg", upload_to="profile_pictures")

    def __str__(self) -> str:
        return self.user.username