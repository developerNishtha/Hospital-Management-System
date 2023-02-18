from django import forms
from opd_pfsh.models import opd_pfsh

class Empforms(forms.ModelForm):
   class Meta:
        model=opd_pfsh
        fields="__all__"


