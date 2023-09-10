from unicodedata import name
from django.db import models


# Create your models
# here.

class Logger(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    time_log = models.TimeField()

    def __str__(self):
        return self.username + " - " + self.password + " - " + self.shift + " - " + str(self.time_log)


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    reservation_time = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=1000)



class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    offer = models.BooleanField(default=False)
    vibeCheck = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " - " + str(self.price) + " - " + self.description + " - " + str(self.offer) + " - " + str(
            self.vibeCheck)


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ElMenu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.name + " - " + str(self.price) + " - " + str(self.category)


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)