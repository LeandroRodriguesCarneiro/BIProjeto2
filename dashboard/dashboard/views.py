from django.shortcuts import render
from django.http import HttpResponse

from data_load.models import Game

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')

def test(request):
    if request.method == 'GET':
        games = Game.objects.all()[:100]

        context = {
            'games': games
        }

        return render(request, 'test.html', context)