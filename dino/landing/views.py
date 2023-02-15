import imp
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "landing/index.html"

class GameView(TemplateView):
    template_name = "landing/dino_run.html"