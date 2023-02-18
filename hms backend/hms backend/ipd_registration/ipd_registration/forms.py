from django import forms
from ipd_registration.models import ipd_registration

class Empforms(forms.ModelForm):
   class Meta:
        model=ipd_registration
        fields="__all__"