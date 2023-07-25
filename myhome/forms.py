from django import forms
from .models import SubmitProperty

class SubmitPropertyForm(forms.ModelForm):
    class Meta:
        # automatically generating form fields for all the fields in the "SubmitProperty" model. 
        model = SubmitProperty
        fields = '__all__'
