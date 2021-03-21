from django.shortcuts import render
from django.views.generic import CreateView
from .forms import EventForm

# Create your Event here
class EventCreateView(CreateView):
    form_class = EventForm
    template_name = 'form.html'
    success_url = '/'