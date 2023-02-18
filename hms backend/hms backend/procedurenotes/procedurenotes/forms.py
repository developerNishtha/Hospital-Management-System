from django import forms
from procedurenotes.models import procedurenotesmodel

class Empforms(forms.ModelForm):
   class Meta:
        model=procedurenotesmodel
        fields="__all__"


