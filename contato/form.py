from django import forms
from contato.models import Occurrence


class OccurrenceForm(forms.ModelForm):
    obsercacao = forms.CharField(required=False)

    class Meta:
        model = Occurrence
        exclude = ('condomino',)