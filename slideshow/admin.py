# -*- coding:utf-8-*-
from django.contrib import admin
from slideshow.models import SlideHome
from django.contrib import admin


class SlideHomeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data','imagem')
    list_filter = ('titulo', 'data')

    def imagem(self, obj):
        img = u"<img src='%s%s' heith='50' width='50'/>" % ('/media/', obj.foto)
        return img
    imagem.allow_tags = True


admin.site.register(SlideHome, SlideHomeAdmin)
