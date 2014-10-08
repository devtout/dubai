from django.contrib import admin
from usuario.models import Condomino

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'is_active', 'status_morador', 'bloco', 'numero')
    list_filter = ('is_active', 'bloco', 'status_morador')

admin.site.register(Condomino, UsuarioAdmin)