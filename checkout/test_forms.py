from django.test import TestCase
from products.models import Product, Brand, Product_Category, Skin_Concern
from .forms import OrderForm


class TestOrderForm(TestCase):
    """ Tests for required fields for Order Form """

    def test_full_name_required(self):
        """ Test full_name is required """
        form = OrderForm({'full_name': ''})
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0],
                         'This field is required.')

    def test_email_required(self):
        """ Test email is required """
        form = OrderForm({'email': ''})
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')

    def test_phone_number_required(self):
        """ Test phone_number is required """
        form = OrderForm({'phone_number': ''})
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0],
                         'This field is required.')

    def test_street_address1_required(self):
        """ Test street_address1 is required """
        form = OrderForm({'street_address1': ''})
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0],
                         'This field is required.')

    def test_town_or_city_required(self):
        """ Test town_or_city is required """
        form = OrderForm({'town_or_city': ''})
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0],
                         'This field is required.')

    def test_country_required(self):
        """ Test country is required """
        form = OrderForm({'country': ''})
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0],
                         'This field is required.')
