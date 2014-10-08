from django.shortcuts import render
from django.http import request
from django.shortcuts import render_to_response
from django.template import RequestContext
from dubai_.forms import ContatoForm, Contato


def contato(request):
    form = ContatoForm()
    data = {}
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        data['form'] = form
        if form.is_valid():
            contato = Contato()
            contato.nome = form.cleaned_data['nome']
            contato.sobrenome = form.cleaned_data['sobrenome']
            contato.email = form.cleaned_data['email']
            contato.mensagem = form.cleaned_data['mensagem']
            contato.save()
            form = ContatoForm()
        else:
            data['erro'] = 'Erro'
    return render_to_response("contacts.html", {'form':form},
                              context_instance=RequestContext(request))
