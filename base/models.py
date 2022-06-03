from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to="items_media")
    qnt = models.IntegerField(default=0)
    size = models.CharField(max_length=20, null=False)
    price = models.FloatField(default="set by agreement")
    
    def __str__(self):
        return self.name