from django.db import models

# Create your models here.
class MyUser(models.Model()):
    def __init__(self):
        return
    def __str__(self):
        return self.name
