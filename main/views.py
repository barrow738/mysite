from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return HttpResponse("<h1>Tech with tim tutorial</h1>")


def view(response):
    return HttpResponse("<h1>This is the first view which is another page</h1>")
