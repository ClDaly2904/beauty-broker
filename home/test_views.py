from django.test import TestCase


class TestViews(TestCase):
    """
    Test for the if the home page loads
    """

    def test_home_index_page(self):
        """ Test home page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
