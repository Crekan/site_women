from django.urls import path
from women.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='show_post'),
]
