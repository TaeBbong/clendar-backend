from .models import SpotSchedule
from rest_framework import serializers

class SpotScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpotSchedule
        fields = ['url', 'title', 'date', 'spot',]