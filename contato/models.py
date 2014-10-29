# -*- coding:utf-8-*-
from django.db import models
from usuario.models import Condomino


class Contato(models.Model):
    condomino = models.ForeignKey(Condomino)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.nome


class Occurrence(models.Model):
    class Meta:
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'
    condomino = models.ForeignKey(Condomino, verbose_name='Condômino')
    ocorrencia = models.CharField(max_length=50, verbose_name='Ocorrência')
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True, editable=False)
    atendida = models.BooleanField(default=False)
    obsercacao = models.TextField(verbose_name='Observação')

    def __unicode__(self):
        return self.ocorrencia