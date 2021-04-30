import random,os
from django.db import models
from django.db.models.signals import pre_save
from Maw.rans import unique_slug_generator,unique_code_generator

# Create your models here.
class Merchant(models.Model):
    name = models.CharField(max_length=120, blank=True,null=True)
    email = models.EmailField(max_length=120, blank=True)
    phone = models.CharField(max_length=39, blank=True)
    location = models.CharField(max_length=120, blank=True)
    inventory = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.name



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext 

def upload_image_path(instance,filename):
    new_filename = random.randint(1, 392003992)
    name,ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'spaces/{new_filename}/{final_filename}'


class Receipt(models.Model):
    status = (
        ('Ready','Ready'),
        ('Ready','Ready'),
        ('Ready','Ready')
    )
    account = (
        ("Cash on Hand", "Cash on Hand"),
        ("Cash from Bank", "Cash from Bank"),
        ("Cheque Payment", "Cheque Payment"),
        ("Momo Transaction", "Momo Transaction"),
    )
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=status, blank=True, default='Ready', max_length=120)
    # merchant = models.ForeignKey(Merchant,on_delete=models.CASCADE),
    account = models.CharField(choices=account, max_length=120, blank=True)
    slug = models.SlugField(blank=True)
    code = models.CharField(max_length=120, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00, blank=True)
    doc = models.FileField(upload_to=upload_image_path, null=True, blank=True)


def model_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.code:
        instance.code = unique_code_generator(instance)

pre_save.connect(model_pre_save_receiver, sender=Receipt)
