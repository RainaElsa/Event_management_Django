from django import forms
from .models import Fillform

class Eventform(forms.ModelForm):
    class Meta:
        model= Fillform
        fields=['fullname','email','phone']