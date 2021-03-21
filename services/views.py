from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SpaceForm,ProgramForm

# Create your Space here
class SpaceCreateView(CreateView):
    form_class = SpaceForm
    template_name = 'form.html'
    success_url = '/'



# Create your Program here
class ProgramCreateView(CreateView):
    form_class = ProgramForm
    template_name = 'form.html'
    success_url = '/'