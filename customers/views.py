from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SpaceuserForm,ParticipantForm


# Create your Spaceuser here
class SpaceuserCreateView(CreateView):
    form_class = SpaceuserForm
    template_name = 'form.html'
    success_url = '/'



# Create your Participant here
class ParticipantCreateView(CreateView):
    form_class = ParticipantForm
    template_name = 'form.html'
    success_url = '/'
