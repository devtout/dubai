# -*- coding:utf-8-*-
from django.contrib.auth.hashers import make_password
from usuario.models import Condomino
from usuario.forms import CadastroForm, AuthenticationForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, logout, login, get_user


def register(request):
    form = CadastroForm
    data = {}
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        data['form'] = form
        if form.is_valid():
            cadastro = Condomino()
            cadastro.first_name = form.cleaned_data['first_name']
            cadastro.last_name = form.cleaned_data['last_name']
            cadastro.identidade = form.cleaned_data['identidade']
            cadastro.cpf = form.cleaned_data['cpf']
            cadastro.email = form.cleaned_data['email']
            cadastro.username = form.cleaned_data['username']
            cadastro.password = make_password(form.cleaned_data['password'])
            cadastro.telefone = form.cleaned_data['telefone']
            cadastro.status_morador = form.cleaned_data['status_morador']
            cadastro.bloco = form.cleaned_data['bloco']
            cadastro.numero = form.cleaned_data['numero']
            cadastro.is_staff = False
            cadastro.is_active = False
            cadastro.save()
            form = CadastroForm()
            data['message'] = 'Cadastro realizado com sucesso.'
            data['spam'] = 'Aguarde a aprovação do administrador.'
            data['detail'] = 'Seu cadastro foi concluído com sucesso. A partir de agora, o acompanhamento do seu condomínio ficará mais ágil e prático.'
            return render_to_response("message.html", {'data':data},
                                      context_instance=RequestContext(request))
        else:
            data['erro'] = 'Erro'
    return render_to_response("register.html", {'form':form},
                              context_instance=RequestContext(request))


def login_view(request):
    form = AuthenticationForm
    error = {}
    error['flag'] = False
    error['message'] = ''
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                data = {}
                data['message'] = 'Login Efetuado com Sucesso.'
                data['spam'] = request.user.username
                # Redireciona para a pagina de sucesso.
                return render_to_response('message.html', {'data': data}, context_instance=RequestContext(request))
            else:
                error['flag'] = True
                error['message'] = 'Sua conta está desabilitada. Por favor, espere a ativação do Administrador.'
                # Retorna mensagem de erro de conta desativada.
                return render_to_response('login.html', {'form': form, 'error': error}, context_instance=RequestContext(request))
        else:
            error['flag'] = True
            error['message'] = 'Usuário e senha não conferem.'
            # Retorna mensagem de login invalido.
            return render_to_response('login.html', {'form':form, 'error':error}, context_instance=RequestContext(request))
    return render_to_response('login.html', {'form':form}, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    data = {}
    data['message'] = 'Logoff efetuado com sucesso.'
    return render_to_response('message.html', {'data': data}, context_instance=RequestContext(request))