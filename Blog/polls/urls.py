from django.urls import path
from .views import index, news, about, contact


urlpatterns = [
    path('', index, name='index'),
    path('news/', news, name='news'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
