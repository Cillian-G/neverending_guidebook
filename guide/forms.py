from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Region, Location


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ('name',)


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('title', 'slug', 'country', 'content', 'image')
        widgets = {
            'content': SummernoteWidget()
        }
