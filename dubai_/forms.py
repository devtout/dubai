from django import forms
from django.forms.models import ModelForm
from django.http import request
from contato.models import Contato
from cadastro.models import Cadastro


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro


