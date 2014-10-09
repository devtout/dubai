from django import forms
from contato.models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato