from unicodedata import name
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Contact Number', max_length=15)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    datetime = models.DateTimeField('Date and Time of Reservation')
    count = models.IntegerField('Number of People')
    notes = models.TextField('Special Requests', blank=True)

    def __str__(self):
        return self.person.name


class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return self.first_name
    
