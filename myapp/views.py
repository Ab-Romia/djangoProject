from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def needs(request):
    wants = """
    <li>Ice Cream : mega and or oreo</li>
    <li>chips cheetos and or sunbites</li>
    <li>10 eggs</li>
    <li>what else think .....</li>
    """
    return HttpResponse(wants)