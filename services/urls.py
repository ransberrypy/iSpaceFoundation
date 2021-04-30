from django.urls import path
from .views import  SpaceCreateView,SpaceDetailView, ProgramCreateView, ProgramDetailView

urlpatterns = [
    path('spaces/create', SpaceCreateView.as_view(), name='add-space'),
    path('spaces/<slug>', SpaceDetailView.as_view(), name='space-detail'),

    # Programs
    path('programs/create', ProgramCreateView.as_view(), name='create-program'),
    path('program/<slug>', ProgramDetailView.as_view(), name='program-detail'),

]