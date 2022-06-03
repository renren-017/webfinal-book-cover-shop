from django.shortcuts import render
from .models import Item

def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "base\home.html", context)
