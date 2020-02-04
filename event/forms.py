from django import forms
from .models import Events


class EventModelForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = [
            'username',
            'title',
            'text',
            'city',
            'date_from',
            'date_to',
            'clock_from',
            'clock_to',
        ]
