from django import forms

from .models import Spaceuser,Participant


class SpaceuserForm(forms.ModelForm):
    class Meta:
        model = Spaceuser
        fields = '__all__'


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
