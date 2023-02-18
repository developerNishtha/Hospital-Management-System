from django import forms
from round_notes.models import round_notes

class Empforms(forms.ModelForm):
   class Meta:
        model=round_notes
        fields="__all__"


    