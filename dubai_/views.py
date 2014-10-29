# coding: utf-8
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from imprensa.views import news_front
from slideshow.views import slide_home


def index(request):
    dados = {}
    dados['slider'] = slide_home()
    dados['news'] = news_front()
    print dados['slider']
    return render_to_response("index.html", dados,
                              context_instance=RequestContext(request))