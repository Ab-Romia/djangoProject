from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Welcome Home!")


def menu(request):
    return HttpResponse("Here is the menu")


def about(request):
    return HttpResponse("there is the alot to know about")


def book(request):
    return HttpResponse("Do you want to make a booking?")
