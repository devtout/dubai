from django import forms
from django.http import request
from contato.models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato


