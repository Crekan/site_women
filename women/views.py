from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from women.forms import *
from women.models import *


def index(request):
    data = {
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', data)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'post': post,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', data)


def about(request):
    return render(request, 'women/about.html')


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавление поста')
    else:
        form = AddPostForm()

    data = {
        'form': form,

    }
    return render(request, 'women/addpage.html', data)


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)
