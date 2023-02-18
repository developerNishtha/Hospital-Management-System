from django import forms
from diagnosis.models import Empmodel

class Empforms(forms.ModelForm):
   class Meta:
        model=Empmodel
        fields="__all__"


