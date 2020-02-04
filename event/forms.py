from django import forms
from .models import Events, Comment


class EventModelForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = [
            'username', 'title', 'text', 'city', 'date_from', 'date_to', 'clock_from', 'clock_to',
        ]


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'username', 'text',
        ]
