from django.contrib import admin
from .models import Reservation, Person, Employees

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Person)
admin.site.register(Employees)
