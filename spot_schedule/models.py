from django.db import models
from spot.models import Spot

# Create your models here.
class SpotSchedule(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    spot = models.ForeignKey(Spot, related_name="schedules", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.spot}, {self.title}: {str(self.date)}'
    