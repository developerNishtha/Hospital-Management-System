from django import forms
from expenseentry.models import expenseentrymodel

class Empforms(forms.ModelForm):
   class Meta:
        model=expenseentrymodel
        fields="__all__"


