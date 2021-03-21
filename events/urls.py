from django.urls import path
from .views import  EventCreateView

urlpatterns = [
    path('events/create', EventCreateView.as_view(), name='create-event')

]