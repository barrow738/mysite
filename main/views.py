from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.
def index(response, id):
    ls = TodoList.objects.get(id=id)
    # return HttpResponse("<h1>%s</h1>" %ls.name)
    # return render(response, "main/base.html", {"name": ls.name})
    # return render(response, "main/base.html", {})
    return render(response, "main/list.html", {"ls": ls})


def home(response):
    # return render(response, "main/home.html", {"name": "Just testing"})
    return render(response, "main/home.html", {})
