from django.urls import path
from . import views

urlpatterns = [
    path('reservation/', views.ReservationView, name='reservation'),
]
