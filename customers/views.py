from django.shortcuts import render
from django.views.generic import CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import SpaceuserForm,ParticipantForm
from .models import Spaceuser, Participant

# Create your Spaceuser here
class SpaceuserCreateView(LoginRequiredMixin,CreateView):
    form_class = SpaceuserForm
    template_name = 'form.html'
    success_url = '/'

    # def form_valid(self,form):
    #     instance = form.save(commit=False)
    #     instance.team_member = self.request.user 
    #     return super(SpaceuserCreateView,self).form_valid(form)


class SpaceuserDetailView(DetailView):
    queryset = Spaceuser.objects.all()



# Create your Participant here
class ParticipantCreateView(LoginRequiredMixin, CreateView):
    form_class = ParticipantForm
    template_name = 'form.html'
    success_url = '/'

    # def form_valid(self,form):
    #     instance = form.save(commit=False)
    #     instance.team_member = self.request.user 
    #     return super(ParticipantCreateView, self).form_valid(form)


class ParticipantDetailView(DetailView):
    queryset = Participant.objects.all()
