from django.db import models
from django.db.models.signals import pre_save

from services.models import Space
from .utils import unique_revenue_code_generator


# Create your models here.
class Booking(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE, blank=True)
    amount = models.IntegerField()
    internet_code = models.CharField(max_length=12, blank=True)
    revenue_code = models.SlugField(blank=True, null=True)
    on =  models.DateTimeField(auto_now_add=True)
    to = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.space)


def bookings_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.revenue_code:
        instance.revenue_code = unique_revenue_code_generator(instance)

pre_save.connect(bookings_pre_save_receiver, sender=Booking)