from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('button',views.button, name='button'),
    path('cards',views.cards, name='cards'),
]