from django.urls import path

from Servicios import views

urlpatterns = [
    path('home', views.home, name='Home'),
    path('deck', views.listarPost, name='Deck'),
    path('history', views.history, name='History'),

]