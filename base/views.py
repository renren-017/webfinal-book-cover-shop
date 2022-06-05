from django.shortcuts import render
from .models import Item

def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "base/home.html", context)

def about(request):
    return render(request, "base/about.html")


def contacts(request):
    return render(request, "base/contacts.html")
