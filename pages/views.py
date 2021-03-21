from django.shortcuts import render
from django.views.generic import ListView,CreateView

# models import
from .models import Inquiry,Birthday
from services.models import Space,Program
from events.models import Event
from customers.models import Participant,Spaceuser

# Forms import
from .forms import InquiryForm,BirthdayForm


# Create your views here.
class HomeView(ListView):    
    template_name = 'index.html'
    queryset = Inquiry.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['birthday_list'] = Birthday.objects.all()
        context['space_list'] = Space.objects.all()
        context['program_list'] = Program.objects.all()
        context['event_list'] = Event.objects.all()
        context['spaceuser_list'] = Spaceuser.objects.all()
        context['participant_list'] = Participant.objects.all()
        # And so on for more models
        return context


# Create your Inquiry here
class InquiryCreateView(CreateView):
    form_class = InquiryForm
    template_name = 'form.html'
    success_url = '/'


# Create your Birthday here
class BirthdayCreateView(CreateView):
    form_class = BirthdayForm
    template_name = 'form.html'
    success_url = '/'
