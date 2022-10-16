from django.db.models import Count
from django.core.cache import cache

from women.models import *


class DataMixin:
    paginate_by = 3

    def get_user_context(self, *args, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Categories.objects.annotate(Count('women'))
            cache.set('cats', cats, 60)

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
