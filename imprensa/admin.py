from django.contrib import admin
from imprensa.models import News, Gallery, Album, Download


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


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo',)
    list_filter = ('tipo',)
    search_fields = ('nome',)


class DownloadAdmin(admin.ModelAdmin):
    list_display = ('album', 'titulo', 'data', 'descricao', 'arquivo')
    #list_filter = ('album',)
    search_fields = ('descricao', 'titulo',)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'album':
            kwargs['queryset'] = Album.objects.filter(tipo='1')
        return super(DownloadAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(News, NewsAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Download, DownloadAdmin)
