from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse("<h1>Tech with tim tutorial</h1>")

def view(response):
    return HttpResponse("<h1>This is the first view</h1>")
# Create your views here.
