from django import forms
from homepage.models import homepagemodel

class Empforms(forms.ModelForm):
   class Meta:
        model=homepagemodel
        fields="__all__"


