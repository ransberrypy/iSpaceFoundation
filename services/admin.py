from django.contrib import admin
from .models import Program,Space
# Register your models here.


class SpaceAdmin(admin.ModelAdmin):
    list_display=('name','price')

admin.site.register(Space,SpaceAdmin)


class ProgramAdmin(admin.ModelAdmin):
    list_display=("name",'slug','facilitator','cohort')

admin.site.register(Program, ProgramAdmin)