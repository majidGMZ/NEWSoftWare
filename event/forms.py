from django import forms
from .models import Events, Comment, Discussion, CommentDiscussion,MemberEvent
from account.models import Account

class EventModelForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = [
             'title', 'text', 'city', 'date_from', 'date_to', 'clock_from', 'clock_to',
        ]


class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
             'text',
        ]


########discussion######


class DiscussionModelForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = [
             'title', 'text', 'city',
        ]


class CommentDiscussionModelForm(forms.ModelForm):
    class Meta:
        model = CommentDiscussion
        fields = [
             'text',
        ]


class JoinEventModelForm(forms.ModelForm):
    class Meta:
        model = MemberEvent
        fields = [

        ]
