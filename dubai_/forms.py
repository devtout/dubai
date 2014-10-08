from AptUrl.Helpers import _
from time import timezone
import datetime
from django import forms
from contato.models import Contato
from usuario.models import Condomino


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato


class CadastroForm(forms.ModelForm):
    last_login = forms.DateTimeField(required=False)
    date_joined = forms.DateTimeField(required=False)
    class Meta:
        model = Condomino


class AuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = ['email', 'password']