# -*- coding:utf-8-*-
import os
import datetime
from django.db import models
from django.db.models import signals
from PIL import Image
from django.core.urlresolvers import reverse
from django.db.models.fields.files import FileField
from dubai.settings import STATIC_ROOT

WIDTH = 720
HEIGHT = 480


def upload_to_foto(instance, name):
    extensao = os.path.splitext(name)[-1]
    data = datetime.datetime.now()
    horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    return os.path.join('imprensa','fotos', '%s%s'%(horario, extensao))


def upload_to_audio(instance, name):
    extensao = os.path.splitext(name)[-1]
    data = datetime.datetime.now()
    horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    return os.path.join('imprensa','audio', '%s%s'%(horario, extensao))


def upload_to_download(instance, name):
    extensao = os.path.splitext(name)[-1]
    data = datetime.datetime.now()
    horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    return os.path.join('imprensa','download', '%s%s'%(horario, extensao))


class Album(models.Model):
    class Meta:
        verbose_name_plural = "Albuns"
    TITLE_TP = (
        ('1','DOCUMENTO'),
        ('2','VIDEO'),
        ('3','AUDIO'),
        #('4','DOWNLOAD'),
    )

    tipo = models.CharField(max_length=1, choices=TITLE_TP)
    nome = models.CharField(max_length=60, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')

    def __unicode__(self):
        return u'%s' % (self.nome)

    def get_downloads(self):
        downloads = Download.objects.filter(album=self).order_by('-id')
        return downloads or None

    def slug(self):
        return slugify(self.nome)


class Download(models.Model):
    album = models.ForeignKey(Album)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    data = models.DateTimeField(auto_now_add=True,editable=False)
    descricao = models.CharField(max_length=140, blank=True, null=True, verbose_name='Descrição')
    arquivo = FileField(upload_to=upload_to_download, max_length=255, verbose_name=u'Arquivo')

    def __unicode__(self):
        return u'%s' % (self.titulo)

    def get_extensao(self):
        return self.arquivo.path.split('.')[-1]

    def icone_existe(self):
        extensao = self.arquivo.path.split('.')[-1]
        try:
            image = Image.open(os.path.join(STATIC_ROOT, os.path.join('imprensa', os.path.join('images', '%s.png' % extensao))))
            return True
        except Exception, e:
            print e
            return False


class News(models.Model):
    class Meta:
        verbose_name = 'Publicidade'
        verbose_name_plural = 'Publicidade'
    titulo = models.CharField(max_length=25, verbose_name='Título')
    texto = models.TextField()	
    foto = models.ImageField(upload_to=upload_to_foto, max_length=255, verbose_name=u'Foto', blank=False, null=False)
    url = models.CharField(max_length=150, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField("slug", max_length=150, editable=False)

    def get_absolute_url(self):
        return reverse('imprensa.views.news', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.titulo


class Gallery(models.Model):
    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galeria'
    titulo = models.CharField(max_length=25,verbose_name='Título')
    foto = models.ImageField(upload_to=upload_to_foto, max_length=255, verbose_name=u'Foto', blank=False, null=False)
    data = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.titulo


def foto_post_save(signal, instance, sender, **kwargs):
    arq = sender.objects.get(foto=instance.foto)
    image = Image.open(arq.foto.path)
    imageresize = image.resize((WIDTH,HEIGHT), Image.ANTIALIAS)
    imageresize.save(arq.foto.path, 'JPEG', quality=100)


def foto_pre_delete(signal, instance, sender, **kwargs):
    arq = sender.objects.get(foto=instance.foto)
    if os.path.exists(arq.foto.path):
        os.remove(arq.foto.path)

from django.template.defaultfilters import slugify


def news_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.titulo)
        novo_slug = slug
        contador = 0

        while News.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)

        instance.slug = novo_slug


signals.pre_save.connect(news_pre_save, sender=News)
signals.post_save.connect(foto_post_save, sender=News)
signals.pre_delete.connect(foto_pre_delete, sender=News)

signals.post_save.connect(foto_post_save, sender=Gallery)
signals.pre_delete.connect(foto_pre_delete, sender=Gallery)