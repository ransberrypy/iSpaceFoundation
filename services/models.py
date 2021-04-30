import random, os 
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from Maw.rans import unique_slug_generator


User = settings.AUTH_USER_MODEL


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
class Space(models.Model):
    # team_member = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, default="Our Spaces")
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, default="About Space")
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'services/spaces/{self.slug}'
        # return reverse('space-detail')
 

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

    def get_absolute_url(self):
        return f'services/program/{self.slug}'
        # return reverse('program-detail')
    
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