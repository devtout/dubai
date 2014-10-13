# -*- coding:utf-8-*-
from django import forms
from usuario.models import Condomino


class CadastroForm(forms.ModelForm):
    last_login = forms.DateTimeField(required=False)
    date_joined = forms.DateTimeField(required=False)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numero = forms.CharField(required=True)

    class Meta:
        model = Condomino


class AuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = ['email', 'password']