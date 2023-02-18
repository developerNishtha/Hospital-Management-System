from django import forms
from ipd_complain.models import ipd_complainmodel

class Empforms(forms.ModelForm):
   class Meta:
        model=ipd_complainmodel
        fields="__all__"