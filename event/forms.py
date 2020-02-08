from django import forms
from .models import Events, Comment, Discussion, CommentDiscussion


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


########discussion######


class DiscussionModelForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = [
            'username', 'title', 'text', 'city',
        ]


class CommentDiscussionModelForm(forms.ModelForm):
    class Meta:
        model = CommentDiscussion
        fields = [
            'username', 'text',
        ]
