from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name
        
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_drescription = models.CharField(max_length=200)
    #image field
    image = models.ImageField(upload_to="pictures/", default="Images/None/Noimg.jpg")