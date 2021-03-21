from django.db import models
from django.db.models.signals import pre_save
from Maw.utils import unique_slug_generator

# Create your models here.
class Inquiry(models.Model):
    name = models.CharField(max_length=129, blank=False)
    telephone = models.CharField(max_length=120, blank=False)
    slug = models.SlugField(blank=True, null=True)
    details = models.TextField(blank=False)
    called_back = models.BooleanField(default=False)
    feedback_details = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Birthday(models.Model):
    name = models.CharField(max_length=120)
    dob = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name



def inquiry_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(inquiry_pre_save_receiver, sender=Inquiry)