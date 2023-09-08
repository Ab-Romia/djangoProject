from django.contrib import admin
from .models import Menu, MenuCategory, ElMenu
# Register your models here.

admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(ElMenu)