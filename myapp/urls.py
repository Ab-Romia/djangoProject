from django.urls import path
from . import views

urlpatterns = [
    path('wants/', views.needs),
]
