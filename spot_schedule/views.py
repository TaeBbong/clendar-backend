from rest_framework import viewsets

from .models import SpotSchedule
from .serializers import SpotScheduleSerializer


class SpotScheduleViewSet(viewsets.ModelViewSet):
    queryset = SpotSchedule.objects.all()
    serializer_class = SpotScheduleSerializer
