from unicodedata import name
from django.db import models


# Create your models
# here.

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Contact Number', max_length=15)
    datetime = models.DateTimeField('Date and Time of Reservation')
    count = models.IntegerField('Number of People')
    notes = models.TextField('Special Requests', blank=True)
