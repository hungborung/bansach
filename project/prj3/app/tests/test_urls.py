from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import categorydetail,productdetail
import unittest
class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('categorydetail', args=['1'])
        self.response = self.client.get(url)
        self.assertEquals(self.response.status_code, 200)