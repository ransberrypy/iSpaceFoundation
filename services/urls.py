from django.urls import path
from .views import  SpaceCreateView,ProgramCreateView

urlpatterns = [
    path('spaces/create', SpaceCreateView.as_view(), name='add-space'),
    path('programs/create', ProgramCreateView.as_view(), name='create-program')

]