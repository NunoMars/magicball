from django.test import TestCase
from django.urls import reverse


class IndexPagesTest(TestCase):
    def test_index_page(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "ball8/ball8.html")
        self.assertEqual(response.status_code, 200)
