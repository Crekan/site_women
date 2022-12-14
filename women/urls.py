from django.views.decorators.cache import cache_page
from django.urls import path
from women.views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logou/', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='show_post'),
    path('category/<slug:cat_slug>/', WomenCategories.as_view(), name='show_category'),
]
