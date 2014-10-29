from django.shortcuts import render_to_response
from django.template import RequestContext
from imprensa.models import Download, Album
from models import News, Gallery


def news(request):
    news = News.objects.all().order_by('-id')
    return render_to_response("index.html", {'news': news, 'ultimas':news[:4]}, context_instance=RequestContext(request))


def news_front():
    return News.objects.all().order_by('-id')[:4]


def news_detail(request, slug):
    return render_to_response("news_detail.html", {'new': News.objects.get(slug=slug), 'last_news': News.objects.all().order_by('-id')[:3]}, context_instance=RequestContext(request))


def gallery(request):
    return render_to_response("gallery.html", {'gallery': Gallery.objects.all().order_by('-id')}, context_instance=RequestContext(request))


def album(request):
    return render_to_response("album.html", {'album': Album.objects.all().filter(tipo='1').order_by('-id')}, context_instance=RequestContext(request))


def download(request, id):
    return render_to_response("download.html", {'download': Download.objects.all().filter(album=id).order_by('-id')}, context_instance=RequestContext(request))