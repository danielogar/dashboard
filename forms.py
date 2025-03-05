from django import forms
from .models import ConfigSettings

class ConfigForm(forms.ModelForm):
    class Meta:
        model = ConfigSettings
        fields = ['name', 'value']
