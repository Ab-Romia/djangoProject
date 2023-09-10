from django import forms
from .models import Logger, Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
