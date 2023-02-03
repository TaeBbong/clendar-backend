from rest_framework import viewsets

from .models import UserSchedule
from .serializers import UserScheduleSerializer


class SpotViewSet(viewsets.ModelViewSet):
    queryset = UserSchedule.objects.all()
    serializer_class = UserScheduleSerializer
