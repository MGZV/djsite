from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    posts = Player.objects.all()
    return render(request, 'player/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'player/about.html', {'menu': menu, 'title': 'О сайте'})


def archive(request, year):
    if int(year) > 2020:
        return redirect('home')
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')