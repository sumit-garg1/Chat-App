from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
#  Create your views here.
@login_required
def rooms(request):
    rooms=Room.objects.all()
    return render(request, "rooms.html", {'rooms': rooms})
# def home_rooms(request):
#     return render(request,"rooms.html")

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    
    return render(request, "room.html", {'room': room})
