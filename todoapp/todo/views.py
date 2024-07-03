from django.shortcuts import render
from .models import TodoItem

# Create your views here.


def home(request):
    return render(request, "home.html")


def todos(request):
    return render(request, "todos.html", {"todos": TodoItem.objects.all()})
