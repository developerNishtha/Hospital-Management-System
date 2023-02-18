from django import forms
from ot_schedule.models import ot_schedulemodel

class Empforms(forms.ModelForm):
   class Meta:
        model=ot_schedulemodel
        fields="__all__"




