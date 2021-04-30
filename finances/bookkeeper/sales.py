import random,os
from django.db import models
from django.db.models.signals import pre_save
from Maw.rans import unique_slug_generator,unique_code_generator
from customers.models import Client


#file / image upload functionality
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext 

def upload_image_path(instance,filename):
    new_filename = random.randint(1, 392003992)
    name,ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'spaces/{new_filename}/{final_filename}'


# Create your models here.
class Invoice(models.Model):
    customer_details = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=120, blank=True)
    invoice_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    code = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00, blank=True)
    line_total = models.DecimalField(max_digits=10, default=0.00,decimal_places=2, blank=True)
    invoice_doc = models.FileField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.slug

   
def model_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.code:
        instance.code = unique_code_generator(instance)

pre_save.connect(model_pre_save_receiver, sender=Invoice)
