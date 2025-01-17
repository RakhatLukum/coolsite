from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]


def index(request):
    posts = Women.objects.all()
    context = {
        'post' : posts,
        'menu' : menu,
        'title' : 'Главная страница'
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponseNotFound('Добавление статьи')

def contact(request):
    return HttpResponseNotFound('Обратная связь')

def login(request):
    return HttpResponseNotFound('Авторизация')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
