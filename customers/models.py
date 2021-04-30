from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from events.models import Event
from bookings.models import Booking
from Maw.rans import unique_slug_generator

User = settings.AUTH_USER_MODEL

# Create your models here.
class Spaceuser(models.Model):
    # team_member = models.ForeignKey(User, on_delete=models.CASCADE)
    booking= models.ForeignKey(Booking, on_delete=models.CASCADE, blank=True)
    joined_date = models.DateField(auto_now_add=False)
    name = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True)
    phone = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=120, blank=True)
    emergency_contact_name = models.CharField(max_length=120, blank=True)
    emergency_contact = models.CharField(max_length=120, blank=True)
    business_name = models.CharField(max_length=120, blank=True)
    business_reg_number = models.CharField(max_length=120, blank=True)
    # voters_id = models.ImageField()
    # passport_pic = models.ImageField()
    # business_cert = models.ImageField()
    timestamp = models.DateField(auto_now_add=True)
    is_member = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('spaceuser-detail')



class Participant(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,blank=True)
    # team_member = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(blank=True, null=True)
    phone = models.CharField(max_length=120, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    guardian_name = models.CharField(max_length=120, blank=True)
    guardian_contact = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=120, blank=True)
    business_name = models.CharField(max_length=120, blank=True, default="iSpace", help_text='Enter a business name if paticipant was a uwat or attended our program')
    business_type = models.TextField(blank=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('participant-detail')


class Funding(models.Model):
    name = models.ForeignKey(Participant,on_delete=models.DO_NOTHING)
    



class Client(models.Model):
    name = models.CharField(max_length=120, blank=True)
    email = models.EmailField(unique=True,blank=True, max_length=255)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


def model_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(model_pre_save_receiver, sender=Spaceuser)
pre_save.connect(model_pre_save_receiver, sender=Participant)