from django.urls import path
from .views import  InquiryCreateView,BirthdayCreateView

urlpatterns = [
    path('inquiry/create', InquiryCreateView.as_view(), name='create-inquiry'),
    path('birthday/create', BirthdayCreateView.as_view(), name='create-birthday')

]