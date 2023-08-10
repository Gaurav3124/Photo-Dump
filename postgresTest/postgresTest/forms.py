from django import forms
from postgresTest.models import photo

class photoforms(forms.ModelForm):
    class Meta:
        model=photo
        fields="__all__"
