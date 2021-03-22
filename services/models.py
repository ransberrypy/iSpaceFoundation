from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from Maw.utils import unique_slug_generator


User = settings.AUTH_USER_MODEL

# Create your models here.
class Space(models.Model):
    # team_member = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, default="Our Spaces")
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, default="About Space")
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
 

class Program(models.Model):
    # user = models.ForeignKey(User)
    name = models.CharField(max_length=120, blank=True, default="Our Program")
    slug = models.SlugField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    facilitator = models.CharField(max_length=120, blank=True)
    cohort = models.CharField(max_length=120, blank=True, help_text="Which year group")
    classtime = models.TimeField(blank=True, null=True)
    description = models.TextField(blank=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)


    def __str__(self) :
        return self.name
    
def model_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(model_pre_save_receiver, sender=Space)
pre_save.connect(model_pre_save_receiver, sender=Program)


# class Classes(models.Model):
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#     name = models.CharField(max_length=120, blank=True, default="Classes")
#     slug = models.SlugField(blank=True, null=True)
#     classtime = models.TimeField(blank=True, null=True)

#     def __str__(self) :
#         return self.name

# def model_pre_save_receiver(sender,instance,*args,**kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)

# pre_save.connect(model_pre_save_receiver, sender=Classes)