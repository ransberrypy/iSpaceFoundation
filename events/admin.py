from django.contrib import admin

from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('program','who','name','description','number_of_attendants')
    search_fields=('name','description')
    list_per_page = 25

admin.site.register(Event, EventAdmin)