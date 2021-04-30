from django.db import models
from django.db.models.signals import pre_save
from Maw.rans import unique_slug_generator,unique_code_generator
from .purchases import Merchant

class Stock(models.Model):
    seller = models.ForeignKey(Merchant, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=120, blank=True, default='item name')
    slug = models.SlugField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00, blank=True)
    bulk_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00, blank=True)
    quantity = models.CharField(max_length=120,blank=True, null=True, default="100 pieces")
    quantity_remaining = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_checked=models.DateTimeField(auto_now_add=False, blank=True)

    def __str__(self):
        return self.name


def model_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
   

pre_save.connect(model_pre_save_receiver, sender=Stock)
