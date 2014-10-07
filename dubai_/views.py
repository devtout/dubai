# coding: utf-8
from django.contrib.auth import logout
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from slideshow.views import slide_home


def index(request):
    dados = {}
    dados['slider'] = slide_home()
    return render_to_response("index.html", dados,
                              context_instance=RequestContext(request))