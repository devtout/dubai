from django import forms
from contato.models import Occurrence


class OccurrenceForm(forms.ModelForm):
    class Meta:
        model = Occurrence
