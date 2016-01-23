from django.test import TestCase
from model_mommy import mommy

from contatos.models import Contato


class ContatoTest(TestCase):

    def setUp(self):
        self.contato = mommy.make(Contato)

    def test_create(self):
        self.assertEqual(1, self.contato.pk)
