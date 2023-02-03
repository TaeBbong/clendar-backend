from rest_framework import viewsets

from .models import MyUser
from .serializers import MyUserSerializer


class SpotViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
