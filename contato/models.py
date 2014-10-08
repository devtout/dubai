from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=25)
    email = models.EmailField()
    mensagem = models.TextField()

    def __unicode__(self):
        return self.nome
