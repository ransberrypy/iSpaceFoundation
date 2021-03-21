from django import forms

from .models import Space,Program


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = '__all__'


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
