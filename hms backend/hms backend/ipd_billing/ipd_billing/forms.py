from django import forms
from ipd_billing.models import ipd_billingmodel

class Empforms(forms.ModelForm):
   class Meta:
        model=ipd_billingmodel
        fields="__all__"


