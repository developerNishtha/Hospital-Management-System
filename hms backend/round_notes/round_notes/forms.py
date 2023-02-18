from django import forms
from round_notes.models import round_notesmodel

class Empforms(forms.ModelForm):
   class Meta:
        model=round_notesmodel
        fields="__all__"




