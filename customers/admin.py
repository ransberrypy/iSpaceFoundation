from django.contrib import admin
from .models import Participant, Spaceuser

# Register your models here.
class SpaceuserAdmin(admin.ModelAdmin):
    list_per_page = 25

admin.site.register(Spaceuser,SpaceuserAdmin)


class ParticipantAdmin(admin.ModelAdmin):
    list_display=('name','event','phone','email')
    list_filter=('event',)
    list_per_page = 25

admin.site.register(Participant, ParticipantAdmin)