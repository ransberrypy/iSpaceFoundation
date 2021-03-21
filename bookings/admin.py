from django.contrib import admin
from django.contrib import admin

from .models import Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('space','amount','internet_code','revenue_code','available')
    list_filter=('revenue_code',)
    list_editable=('available',)
    search_fields=('amount','internet_code','revenue_code')
    list_per_page = 25

admin.site.register(Booking, BookingAdmin)