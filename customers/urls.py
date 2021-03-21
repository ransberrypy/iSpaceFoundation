from django.urls import path
from .views import  SpaceuserCreateView,ParticipantCreateView

urlpatterns = [
    path('spaceuser/create', SpaceuserCreateView.as_view(), name='add-spaceuser'),
    path('participant/create', ParticipantCreateView.as_view(), name='add-participant')

]