from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Home page") 

def rooms(request):
    return HttpResponse("This is a study room")