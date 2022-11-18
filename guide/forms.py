from .models import Region
from django import forms

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ('name',)