from django import forms
from .models import Reservation, Person


# class PersonForm to take the fields of the name and contact number in the models.py

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'contact']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['datetime', 'count', 'notes']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

