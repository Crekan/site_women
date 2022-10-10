from women.models import *
from django import template

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories(filter=None):
    if not filter:
        return Categories.objects.all()
    else:
        return Categories.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Categories.objects.all()
    else:
        cats = Categories.objects.order_by(sort)

    data = {
        'cats': cats,
        'cat_selected': cat_selected,
    }
    return data


@register.simple_tag(name='get_post')
def get_post(filter=None):
    if not filter:
        return Women.objects.all()
    else:
        return Women.objects.filter(pk=filter)