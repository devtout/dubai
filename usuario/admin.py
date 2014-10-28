from django.contrib import admin
from usuario.models import Condomino


class UsuarioAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'username', 'password', 'is_active', 'date_joined', 'status_morador', 'bloco', 'numero')
    list_display = ('username', 'date_joined', 'is_active', 'status_morador', 'bloco', 'numero')
    list_filter = ('is_active', 'bloco', 'status_morador')
    list_editable = ('is_active',)

admin.site.register(Condomino, UsuarioAdmin)