from django import forms
from opdrx.models import opdrxmodel

class opdrxform(forms.ModelForm):
   class Meta:
        model=opdrxmodel
        fields="__all__"


