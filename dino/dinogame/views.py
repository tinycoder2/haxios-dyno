from django.http import HttpResponse

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy
from dinogame.models import Participant
from .forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")

# view to create a missing person
class ParticipantCreateView(CreateView):
    model = Participant
    form_class = ParticipantCreateForm
    template_name = 'dinogame/create_form.html'
    success_url = reverse_lazy ('list_participant')

# view to list all missing people
class ParticipantListView(ListView):
    # login_url = reverse_lazy('index')
    # logout_url = reverse_lazy('index')
    model = Participant
    template_name = 'dinogame/list.html'
    context_object_name = "participant"
    ordering = ['-score']

class GameView(TemplateView):
    template_name = "dinogame/dino_run.html"