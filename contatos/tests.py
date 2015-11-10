# coding: utf-8

from django.test import TestCase


class UrlsContatosTest(TestCase):

    def setUp(self):
        self.urls = ('/contatos/',)

    def generate_test_url(self, url):
        def test(self, url):
            response = self.client.get(url)
            message = '{} inaccessible'.format(url)
            self.assertEquals(200, response.status_code, message)
        return test(self, url)
