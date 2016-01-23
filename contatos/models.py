from django.db import models
from django.utils.translation import ugettext_lazy as _

from .choices import UF


class Contato(models.Model):
    nome = models.CharField(_('Nome'), max_length=60)
    nascimento = models.DateTimeField(blank=False, null=True)
    telefone_fixo = models.CharField(_('Telefone fixo'), max_length=20)
    telefone_celular = models.CharField(_('Telefone celular'), max_length=20)
    email = models.EmailField(_('E-mail'), max_length=300, unique=True)
    endereco = models.CharField(_('Endereço'), max_length=80)
    complemento = models.CharField(_('Complemento'), max_length=30)
    uf = models.CharField(
        _('UF'), max_length=2, blank=False, null=True, choices=UF
    )
    bairro = models.CharField(_('Bairro'), max_length=20)
    obs = models.TextField(blank=False, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-nome',)
        verbose_name = _('Contato')
        verbose_name_plural = _('Contatos')

    def __str__(self):
        return 'Contato: {}'.format(self.nome)

