from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import condition


def home(request):
    return HttpResponse("Welcome Home!")


def menu(request):
    return HttpResponse("Here is the menu")


def about(request):
    return HttpResponse("there is the alot to know about")


def book(request):
    return HttpResponse("Do you want to make a booking?")


# a view that returns a template containing an input of username and password styled with bootstrap
def login(request):
    return render(request, 'login.html')
