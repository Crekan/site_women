from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from women.models import *


def index(request):
    posts = Women.objects.all()

    data = {
        'posts': posts,
    }
    return render(request, 'women/index.html', data)


def show_post(request, post_id):
    return HttpResponse(f'This is id - {post_id}')


def about(request):
    return render(request, 'women/about.html')


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
