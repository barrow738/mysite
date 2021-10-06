from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.
def index(response, id):
    ls = TodoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" %ls.name)
