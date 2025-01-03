from django.shortcuts import render
from .models import ToDoList
from .forms import CreateNewList
# Create your views here.

def index(response, name):
    ls = ToDoList.objects.get(name = name)
    return render(response, "main/list.html", {"name": ls})

def home(response):
    return render(response, "main/home.html", {"name": "test"})

def create(response):
    # if (response.method == "POST"):
    form = CreateNewList(response.POST)
    return render(response, "main/create.html", {"form": form})