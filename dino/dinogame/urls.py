from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('list-participant/', ParticipantListView.as_view(), name='list_participant'),
    path('create-participant/', ParticipantCreateView.as_view(), name='create_participant'),
    path('', GameView.as_view(), name='dino_run'),
]