from django import forms
from opdcomplain.models import opdcomplainmodel

class Empforms(forms.ModelForm):
   class Meta:
        model=opdcomplainmodel
        fields="__all__"


