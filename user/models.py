from django.db import models
from spot.models import Spot

# Create your models here.
class MyUser(models.Model):
    uid = models.CharField(max_length=100, primary_key=True)
    spots = models.ManyToManyField(Spot, related_name="follower")

    def __str__(self):
        return self.uid
