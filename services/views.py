from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SpaceForm,ProgramForm

# Create your Space here
class SpaceCreateView(LoginRequiredMixin ,CreateView):
    form_class = SpaceForm
    template_name = 'form.html'
    success_url = '/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.team_member = self.request.user 
        return super(SpaceCreateView, self).form_valid(form)


# Create your Program here
class ProgramCreateView(LoginRequiredMixin,CreateView):
    form_class = ProgramForm
    template_name = 'form.html'
    success_url = '/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.team_member = self.request.user 
        return super(ProgramCreateView, self).form_valid(form)