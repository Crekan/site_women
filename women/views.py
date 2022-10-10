from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404

from women.models import *


def index(request):
    data = {
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', data)


def show_post(request, post_id):
    post = get_object_or_404(Women, pk=post_id)

    data = {
        'post': post,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', data)


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


def show_category(request, cat_id):
    data = {
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', data)

