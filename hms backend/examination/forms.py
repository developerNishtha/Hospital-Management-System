from django import forms
from examination.models import OPD_Examination

class Empforms(forms.ModelForm):
   class Meta:
        model=OPD_Examination
        fields="__all__"


    