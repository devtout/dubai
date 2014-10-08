# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, AbstractBaseUser
from django.db import models


class Condomino(User):
    class Meta:
        verbose_name_plural = 'Condôminos'
    BLOCO_TP = (
        ('1','JADE'),
        ('2','SAFIRA')
    )

    STATUS_MORADOR_TP = (
        ('1','PROPRIETÁRIO'),
        ('2','LOCATÁRIO')
    )
    identidade = models.CharField(max_length=25, unique=True)
    cpf = models.CharField(max_length=25, unique=True)
    telefone = models.CharField(max_length=25)
    bloco = models.CharField(max_length=1, choices=BLOCO_TP, verbose_name=unicode('Bloco'))
    status_morador = models.CharField(max_length=1, choices=STATUS_MORADOR_TP, verbose_name=unicode('Status'))
    numero = models.CharField(max_length=25, verbose_name=u'Número')
    def __unicode__(self):
        return u'%s' % (self.first_name)