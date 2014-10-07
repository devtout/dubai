# -*- coding:utf-8-*-
import os
import datetime
from django.db import models
from django.db.models import signals
from django.db.models.fields.files import ImageField, FileField
from django.contrib import admin
from PIL import Image

WIDTH = 720
HEIGHT = 480


def upload_to_foto(instance, name):
    extensao = os.path.splitext(name)[-1]
    data = datetime.datetime.now()
    horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    return os.path.join('slides','fotos', '%s%s'%(horario, extensao))


class SlideHome(models.Model):
    class Meta:
        verbose_name_plural = 'Home'
    data = models.DateTimeField(auto_now_add=True, editable=False)
    titulo = models.CharField(max_length=20,verbose_name='Título')
    foto = models.ImageField(upload_to=upload_to_foto)


def foto_post_save(signal, instance, sender, **kwargs):
    arq = SlideHome.objects.get(foto=instance.foto)
    image = Image.open(arq.foto.path)
    imageresize = image.resize((WIDTH,HEIGHT), Image.ANTIALIAS)
    imageresize.save(arq.foto.path, 'JPEG', quality=100)


def foto_pre_delete(signal, instance, sender, **kwargs):
    arq = SlideHome.objects.get(foto=instance.foto)
    if os.path.exists(arq.foto.path):
        os.remove(arq.foto.path)


signals.post_save.connect(foto_post_save, sender=SlideHome)
signals.pre_delete.connect(foto_pre_delete, sender=SlideHome)