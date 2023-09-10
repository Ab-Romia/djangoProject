from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from django.views.decorators.http import condition
from myapp.forms import LogForm


def book(request):
    form = forms.BookingForm()
    if request.method == "POST":
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)


def form_view(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "form.html", context)


def menu(request):
    return HttpResponse("Here is the menu")


def about(request):
    return HttpResponse("there is the alot to know about")


# a view that returns a template containing an input of username and password styled with bootstrap
def login(request):
    return render(request, 'login.html')
