from django.contrib import admin
from contato.models import Contato
from readOnly import ReadOnlyAdminFields

class ContatoAdmin(ReadOnlyAdminFields, admin.ModelAdmin):
    readonly = ('nome', 'sobrenome', 'email', 'mensagem')
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        #Return nothing to make sure user can't update any data
        pass


admin.site.register(Contato, ContatoAdmin)