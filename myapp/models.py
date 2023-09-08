from unicodedata import name
from django.db import models


# Create your models
# here.
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
