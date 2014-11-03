# -*- coding:utf-8-*-
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext
from contato.form import OccurrenceForm
from contato.models import Occurrence
from dubai.settings import EMAIL_HOST_USER
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
            occurrence.obsercacao
            occurrence.save()
            form = OccurrenceForm()
            data['message'] = 'Ocorrência realizada com sucesso.'
            send_mail('['+occurrence.condomino.get_bloco_display() + ' - ' + occurrence.condomino.numero + '] ' +
                      occurrence.ocorrencia, occurrence.mensagem + '\n\n' + occurrence.condomino.first_name + ' ' +
                      occurrence.condomino.last_name + ' - ' + occurrence.condomino.get_status_morador_display() + '\n' + occurrence.condomino.email + '\n' +
                      occurrence.condomino.telefone, EMAIL_HOST_USER,
                      ['wrnunesneto@gmail.com',], fail_silently=False)
            return render_to_response('message.html', {'data': data}, context_instance=RequestContext(request))
        else:
            data['erro'] = 'Erro'
            return render_to_response("occurrence.html", {'form':form}, context_instance=RequestContext(request))
    return render_to_response("occurrence.html", {'form':form}, context_instance=RequestContext(request))
