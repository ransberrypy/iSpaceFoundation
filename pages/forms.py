from django import forms

from .models import Inquiry, Birthday


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'