from django.test import TestCase
from django.contrib.auth.models import User
from bag.templatetags.bag_tools import calc_subtotal
from .contexts import bag_contents
from products.models import Product


class ViewBagTestViews(TestCase):
    """ Test for the views in Bag app """

    def setUp(self):
        """ Set up objects for testing """

        self.user = User.objects.create(username='admin')

        self.product_1 = Product.objects.create(
            name='Test product 1',
            description='Test description 1',
            price='11',
            rating='1.1',
            ingredients_list='Test ingredients 1',
            line_number='1',
        )

        self.product_2 = Product.objects.create(
            name='Test product 2',
            description='Test description 2',
            price='12',
            rating='1.2',
            ingredients_list='Test ingredients 2',
            line_number='2',
        )

    def test_bag_page(self):
        """ Test products page load """

        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        """ Test products are added to bag """

        response = self.client.post(
            f'/bag/add/{str(self.product_1.pk)}/',
            {'quantity': 2, 'redirect_url': 'view_bag'}
        )
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.product_1.pk)], 2)
        self.assertRedirects(response, '/bag/')

    def test_update_bag(self):
        """ Test functionality to update items in bag """
        # add product to bag
        response = self.client.post(
            f'/bag/add/{str(self.product_1.pk)}/',
            {'quantity': 1, 'redirect_url': 'view_bag'}
        )
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.product_1.pk)], 1)
        self.assertIn('bag', self.client.session)
        self.assertRedirects(response, '/bag/')

        # update quantity of product
        response = self.client.post(
            f'/bag/update/{str(self.product_1.pk)}/',
            {'quantity': 7, 'redirect_url': 'view_bag'}
        )
        bag = self.client.session['bag']
        # check new quantity of product is in bag
        self.assertEqual(bag[str(self.product_1.pk)], 7)
        self.assertIn('bag', self.client.session)

    def test_remove_from_bag(self):
        """ Test CRUD functionality to remove items from bag """

        self.client.post(
                f'/bag/add/{str(self.product_1.pk)}/',
                {'quantity': 2, 'redirect_url': 'view_bag'}
            )
        self.client.post(
                f'/bag/add/{str(self.product_2.pk)}/',
                {'quantity': 2, 'redirect_url': 'view_bag'}
            )
        bag = self.client.session['bag']
        response = self.client.post(f'/bag/remove/{str(self.product_1.pk)}/')
        # check product 1 is no longer in bag
        self.assertNotIn(self.product_1, bag)


class TestBagTools(TestCase):
    """ Test bag tools """

    def test_calc_subtotal(self):
        """ Test calc_subtotal function return correct """

        price = 2
        quantity = 2
        sub_t = 4

        subtotal = calc_subtotal(2, 2)

        self.assertEqual(subtotal, sub_t)
