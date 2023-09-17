from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from .models import Reservation, Person


# Create a reservation view to take the reservation details from the user (name, contact, datetime, count, notes) and save it to the database.

def ReservationView(request):
    if request.method == 'POST':
        person_form = forms.PersonForm(request.POST)
        reservation_form = forms.ReservationForm(request.POST)
        if person_form.is_valid() and reservation_form.is_valid():
            person = person_form.save()
            reservation = reservation_form.save(commit=False)
            reservation.person = person
            reservation.save()
            return HttpResponse('Reservation is successful!')
    else:
        person_form = forms.PersonForm()
        reservation_form = forms.ReservationForm()
    return render(request, 'reservation.html', {'person_form': person_form, 'reservation_form': reservation_form})


def home(request):
    return render(request, "home.html", {})


def register(request):
    return render(request, "register.html", {})


def login(request):
    return render(request, "login.html", {})