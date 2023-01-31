from django.db import models
from user.models import MyUser
from spot.models import Spot

# Create your models here.
class UserSchedule(models.Model):
    date = models.DateField()
    user = models.ForeignKey(MyUser, related_name='schedules', on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user}, {self.date}: {self.spot}'
    