# -*- coding: utf-8 -*-
from encodings.punycode import selective_find
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from dubai.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


class Condomino(User):
    class Meta:
        verbose_name = "Condômino"
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
        return (self.first_name)


def send_mail_condomino(sender, instance, **kwargs):
    if instance.is_active:
        email = instance.email
        send_mail('Solicitação de Cadastro', 'O seu cadastro foi aprovado. Agora você já pode utilizar os serviços do DUBAI RESIDENCE através do site www.condominiodubai.com.br.', EMAIL_HOST_USER, [email,], fail_silently=False)


post_save.connect(send_mail_condomino, sender=Condomino)