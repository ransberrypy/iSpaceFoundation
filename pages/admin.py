from django.contrib import admin
from .models import Inquiry, Birthday

# Register your models here.
class InquiryAdmin(admin.ModelAdmin):
    list_per_page=25
    list_display = ('name',"telephone",'called_back')
    list_editable=('called_back',)

admin.site.register(Inquiry, InquiryAdmin)


class BirthdayAdmin(admin.ModelAdmin):
    list_display = ('name','dob')

admin.site.register(Birthday,BirthdayAdmin)