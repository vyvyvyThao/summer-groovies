from django import forms 
from .models import Class

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = [
            'title',
            'start_date',
            'schedule',
            'description',
            'slots_remaining'
        ]