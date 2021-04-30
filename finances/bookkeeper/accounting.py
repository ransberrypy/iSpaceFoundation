import random,os
from django.db.models.signals import pre_save
from Maw.rans import unique_slug_generator,unique_code_generator
from django.db import models


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext 

def upload_image_path(instance,filename):
    new_filename = random.randint(1, 392003992)
    name,ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'spaces/{new_filename}/{final_filename}'


class Transaction(models.Model):
    account = (
        ("Cash on Hand", "Cash on Hand"),
        ("Cash from Bank", "Cash from Bank"),
        ("Cheque Payment", "Cheque Payment"),
        ("Momo Transaction", "Momo Transaction"),
    )
    category = (
        ("SALES", "SALES"),
        ("INTERNET", "INTERNET"),
        ("OFFICE SUPPLIES", "OFFICE SUPPLIES"),
        ("PAYROLL", "PAYROLL"),
        ("RENT", "RENT"),
        ("REPAIRS", "REPAIRS"),
        ("UTILITIES", "UTILITIES"),
    )
    # type = (
    #     ("Expense","Expense"),
    #     ("Income","Income")
    # )
    date = models.DateField(auto_now_add=True)
    description =  models.TextField(blank=True)
    account = models.CharField(choices=account, max_length=120, blank=True)
    category = models.CharField(choices=category, max_length=120, blank=True)
    slug = models.SlugField(blank=True)
    code = models.CharField(max_length=120, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00, blank=True)
    doc = models.FileField(upload_to=upload_image_path, null=True, blank=True)
    # type = models.CharField(choices=type, max_length=120, blank=True)
    is_match = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    @property
    def name(self):
        return self.description

def model_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.code:
        instance.code = unique_code_generator(instance)

pre_save.connect(model_pre_save_receiver, sender=Transaction)



