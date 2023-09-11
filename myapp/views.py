from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from .models import Reservation


def ReservationView(request):
    if request.method == 'POST':
        form = forms.ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Reservation saved!')
    else:
        form = forms.ReservationForm()
    return render(request, 'reservation.html', {'reservation': form})
