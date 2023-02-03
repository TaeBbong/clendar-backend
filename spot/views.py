from rest_framework import viewsets

from .models import Spot
from .serializers import SpotSerializer


class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
