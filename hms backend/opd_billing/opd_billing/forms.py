from django import forms
from opd_billing.models import opd_billingmodel

class Empforms(forms.ModelForm):
   class Meta:
        model=opd_billingmodel
        fields="__all__"


    