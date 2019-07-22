from django import forms
from erc.models import Event

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