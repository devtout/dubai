from django import forms
from contato.models import Contato
from usuario.models import Condomino


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Condomino


class AuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = ['email', 'password']