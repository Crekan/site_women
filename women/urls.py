from django.urls import path
from women.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]
