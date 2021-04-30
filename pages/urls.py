from django.urls import path
from .views import  InquiryCreateView,BirthdayCreateView, InquiryDetailView

urlpatterns = [
    path('inquiry/create', InquiryCreateView.as_view(), name='create-inquiry'),
    path('birthday/create', BirthdayCreateView.as_view(), name='create-birthday'),
    path('inquiry/<slug>', InquiryDetailView.as_view(), name='inquiry-detail'),


]