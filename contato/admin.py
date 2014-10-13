from django.contrib import admin
from contato.models import Contato, Occurrence
from readOnly import ReadOnlyAdminFields
from usuario.models import Condomino


class ContatoAdmin(ReadOnlyAdminFields, admin.ModelAdmin):
    readonly = ('nome', 'sobrenome', 'email', 'mensagem')
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        #Return nothing to make sure user can't update any data
        pass


class OccurrenceAdmin(admin.ModelAdmin):
    readonly_fields = ('condomino', 'ocorrencia', 'mensagem',)
    list_display = ('ocorrencia', 'atendida', 'data', 'condomino',)
    list_filter = ('data', 'atendida')


admin.site.register(Occurrence, OccurrenceAdmin)
admin.site.register(Contato, ContatoAdmin)