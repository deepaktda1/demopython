from django import forms
from .models import mobile
class mobileform(forms.ModelForm):
    class Meta:
         model=mobile
         fields=['mobname','des','price','img']
