from django.test import TestCase
from .models import Order
from products.models import Product


class TestOrderModels(TestCase):
    """ Tests for the checkout models """

    def setUp(self):

        self.order1 = Order.objects.create(
            order_number='1234567890',
            full_name='Test User',
            email='testuser@email.com',
            phone_number='12345678',
            country='GB',
            postcode='12345',
            town_or_city='Test Town',
            street_address1='Test Street 1',
            county='Test County',
        )

        self.product1 = Product.objects.create(
            line_number='123456789',
            name='Test Product',
            description='Test description',
            ingredients_list='Test ingredients',
            price='26.99',
        )

    def test_order_str_method(self):
        """ Test the order model returns the correct string """

        self.order1 = Order.objects.get(email='testuser@email.com')
        self.assertEqual(str(self.order1), self.order1.order_number)

    def test_checkout_page(self):
        """ test the checkout page """

        session = self.client.session
        session['bag'] = {str(self.product1.pk): 1}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
