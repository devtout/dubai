from django.contrib import admin
from imprensa.models import News, Gallery


class NewsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'imagem')
    list_filter = ('data',)

    def imagem(self, obj):
        img = u"<img src='%s%s' heith='50' width='50'/>" % ('/media/', obj.foto)
        return img
    imagem.allow_tags = True


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'imagem')
    list_filter = ('data',)

    def imagem(self, obj):
        img = u"<img src='%s%s' heith='50' width='50'/>" % ('/media/', obj.foto)
        return img
    imagem.allow_tags = True


admin.site.register(News, NewsAdmin)
admin.site.register(Gallery, GalleryAdmin)
