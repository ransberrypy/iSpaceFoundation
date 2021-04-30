from django.conf import settings
from django.db import models
from services.models import Program
from django.urls import reverse

from django.db.models.signals import pre_save
from Maw.rans import unique_slug_generator

User = settings.AUTH_USER_MODEL

# Create your models here.
class Event(models.Model):
    team_member = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE,blank=True)
    who = models.CharField(max_length=120, blank=True, default='Internal Event',help_text="Name of Organization")
    name = models.CharField(max_length=120, blank=True, help_text="Name of Event")
    slug = models.SlugField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, help_text='What its about, Chair person')
    number_of_attendants = models.IntegerField(blank=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-detail')

def event_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(event_pre_save_receiver, sender=Event)