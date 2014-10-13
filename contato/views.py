from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from contato.form import OccurrenceForm
from contato.models import Occurrence
from dubai_.forms import ContatoForm, Contato
from usuario.models import Condomino


def contact(request):
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

@login_required
def occurrence(request):
    form = OccurrenceForm
    data = {}
    error = {}
    error['flag'] = False
    error['message'] = ''
    if request.method == 'POST':
        form = OccurrenceForm(request.POST)
        data['form'] = form
        if form.is_valid():
            occurrence = Occurrence()
            occurrence.condomino = Condomino.objects.get(username=request.user.username)
            occurrence.ocorrencia = form.cleaned_data['ocorrencia']
            occurrence.mensagem = form.cleaned_data['mensagem']
            occurrence.save()
            form = OccurrenceForm()
        else:
            data['erro'] = 'Erro'
    return render_to_response("occurrence.html", {'form':form}, context_instance=RequestContext(request))