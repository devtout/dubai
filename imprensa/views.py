from django.shortcuts import render_to_response
from django.template import RequestContext
from models import News

def news(request):
    news = News.objects.all().order_by('-id')
    return render_to_response("index.html", {'news': news, 'ultimas':news[:4]},
                              context_instance=RequestContext(request))

def news_front():
    news = News.objects.all().order_by('-id')
    return news[:4]