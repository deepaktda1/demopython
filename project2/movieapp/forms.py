from django import forms
from .models import movie
class MovieForm(forms.ModelForm):
    class Meta:
         model=movie
         fields=['name','des','year','img']