from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BookingSpace(models.Model):
    username = models.CharField(max_length=200)
    email  = models.CharField(max_length=200)
    room = models.CharField(max_length=10)
    time = models.TimeField()
    date = models.DateField()

    class Meta:
        unique_together = ['room', 'time', 'date']



    def __str__(self):
        return self.username







