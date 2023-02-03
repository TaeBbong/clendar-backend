from .models import UserSchedule
from rest_framework import serializers

class UserScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSchedule
        fields = ['url', 'date', 'user', 'spot',]