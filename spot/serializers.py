from .models import Spot
from rest_framework import serializers

class SpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spot
        fields = ['url', 'name', 'location', 'thumbnail', 'color', ]