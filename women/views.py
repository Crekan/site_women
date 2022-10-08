from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from women.models import *


def index(request):
    posts = Women.objects.all()

    data = {
        'posts': posts,
    }

    return render(request, 'women/index.html', data)


def about(request):
    return render(request, 'women/about.html')

def categorise(request, cat_id):
    print(request.GET)
    return HttpResponse(f"<h1>Categories</h1><p>{cat_id}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
