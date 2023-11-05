from django.shortcuts import render
from .models import *
from datetime import date

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def players(request):
    data = {
        "players" : Player.objects.all()
    }

    return render(request, 'players.html', data)

def clubs(request):
    data = {
        "clubs" : Club.objects.all()
    }
    return render(request, 'clubs.html', data)

def u20players(request):
    h_sana = str(date.today())  # "2023-11-03"
    yil = int(h_sana[:4]) - 20  # int("2023") - 20 = 2003
    yangi_sana = h_sana.replace(h_sana[:4], str(yil))  # "2003-11-03"
    data = {
        "players" : Player.objects.filter(tugilgan_yil__gte=yangi_sana
                        ).order_by("-narx", "-tugilgan_yil"),
        "hozirgi_yil" : date.today().year

    }
    return render(request, 'U-20 players.html', data)

def davlat_clublari(request, davlat):
    content = {
        "d_clubs": Club.objects.filter(davlat=davlat.capitalize())
    }
    return render(request, 'davlatlar.html', content)

def c_clubs(request, club):
    data = {
        "t_club" : Player.objects.filter(club__nom  =club.capitalize())
    }
    return render(request, 'country-clubs.html', data)

def h_mavsum(request):
    data = {
        "h_mavsum" : Transfer.objects.filter(mavsum="23-24")
    }
    return render(request, 'latest-transfers.html', data)