from django.shortcuts import render
from cadastro.models import Cadastro
from dubai_.forms import CadastroForm
from django.template import RequestContext
from django.shortcuts import render_to_response


def cadastro(request):
    form = CadastroForm
    data = {}
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        data['form'] = form
        if form.is_valid():
            cadastro = Cadastro()
            cadastro.nome_completo = form.cleaned_data['nome_completo']
            cadastro.identidade = form.cleaned_data['identidade']
            cadastro.cpf = form.cleaned_data['cpf']
            cadastro.email = form.cleaned_data['email']
            cadastro.bloco = form.cleaned_data['bloco']
            cadastro.status_morador = form.cleaned_data['status_morador']
            cadastro.telefone = form.cleaned_data['telefone']
            cadastro.numero = form.cleaned_data['numero']
            cadastro.save()
            form = CadastroForm()
        else:
            data['erro'] = 'Erro'
    return render_to_response("register.html", {'form':form},
                              context_instance=RequestContext(request))
