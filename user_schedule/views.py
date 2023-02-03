from rest_framework import viewsets

from .models import UserSchedule
from .serializers import UserScheduleSerializer


class UserScheduleViewSet(viewsets.ModelViewSet):
    queryset = UserSchedule.objects.all()
    serializer_class = UserScheduleSerializer
