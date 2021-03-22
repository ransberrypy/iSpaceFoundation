from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import SpaceuserForm,ParticipantForm


# Create your Spaceuser here
class SpaceuserCreateView(LoginRequiredMixin,CreateView):
    form_class = SpaceuserForm
    template_name = 'form.html'
    success_url = '/'

    # def form_valid(self,form):
    #     instance = form.save(commit=False)
    #     instance.team_member = self.request.user 
    #     return super(SpaceuserCreateView,self).form_valid(form)


# Create your Participant here
class ParticipantCreateView(LoginRequiredMixin, CreateView):
    form_class = ParticipantForm
    template_name = 'form.html'
    success_url = '/'

    # def form_valid(self,form):
    #     instance = form.save(commit=False)
    #     instance.team_member = self.request.user 
    #     return super(ParticipantCreateView, self).form_valid(form)