# -*- coding: utf-8 -*-
from django.db import models


class Cadastro(models.Model):
    BLOCO_TP = (
        ('1','JADE'),
        ('2','SAFIRA')
    )

    STATUS_MORADOR_TP = (
        ('1','PROPRIETÁRIO'),
        ('2','LOCATÁRIO')
    )
    data = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=unicode('Data'))
    nome_completo = models.CharField(max_length=60)
    identidade = models.CharField(max_length=25)
    cpf = models.CharField(max_length=25)
    email = models.EmailField()
    telefone = models.CharField(max_length=25)
    bloco = models.CharField(max_length=1, choices=BLOCO_TP, verbose_name=unicode('Bloco'))
    status_morador = models.CharField(max_length=1, choices=STATUS_MORADOR_TP, verbose_name=unicode('Status'))
    numero = models.CharField(max_length=25)