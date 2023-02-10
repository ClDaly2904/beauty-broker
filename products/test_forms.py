from django.test import TestCase
from .models import Product, Brand, Product_Category, Skin_Concern
from .forms import ProductForm


class TestProductForm(TestCase):
    """ Tests for required fields for Product Form """

    def test_line_number_required(self):
        """ Test line number is required """
        form = ProductForm({'line_number': ''})
        self.assertIn('line_number', form.errors.keys())
        self.assertEqual(form.errors['line_number'][0],
                         'This field is required.')

    def test_name_required(self):
        """ Test name is required """
        form = ProductForm({'name': ''})
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0],
                         'This field is required.')

    def test_price_required(self):
        """ Test price is required """
        form = ProductForm({'price': ''})
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0],
                         'This field is required.')

    def test_description_required(self):
        """ Test description is required """
        form = ProductForm({'description': ''})
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_ingredients_list_required(self):
        """ Test ingredients_list is required """
        form = ProductForm({'ingredients_list': ''})
        self.assertIn('ingredients_list', form.errors.keys())
        self.assertEqual(form.errors['ingredients_list'][0],
                         'This field is required.')
