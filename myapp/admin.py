from django.contrib import admin
from .models import Menu, MenuCategory, ElMenu, Person, Logger, Booking

# Register your models here.
admin.site.register(Booking)
admin.site.register(Logger)
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(ElMenu)
admin.site.register(Person)
