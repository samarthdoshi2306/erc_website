from django import forms
from erc.models import *

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=[
            'name',
            'problem_statement',
            'video',
            'event_status',
            'content',
            'date',
            'img',
            'filterClass',
        ]


class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields=[
            'image',
            'date',
            'pdf',
            'headline',
        ]