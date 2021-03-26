from django.shortcuts import render
from django.views.generic import CreateView,DetailView
from .forms import EventForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event

# Create your Event here
class EventCreateView(LoginRequiredMixin,CreateView):
    form_class = EventForm
    template_name = 'form.html'
    success_url = '/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.team_member = self.request.user 
        return super(EventCreateView,self).form_valid(form)


class EventDetailView(DetailView):
    queryset = Event.objects.all()