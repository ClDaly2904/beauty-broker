from django.test import TestCase
from .models import Product_Category, Product, Skin_Concern, Brand


class TestModels(TestCase):
    """ Test the models """

    def test_product_category(self):
        """ Test if the product category model returns a string  """
        category = Product_Category.objects.create(
            name='test_category',
            friendly_name="Test Category"
            )
        self.assertEqual(str(category.name), 'test_category')
        self.assertEqual(str(category.friendly_name), 'Test Category')

    def test_skin_concern_category(self):
        """ Test if the skin concern model returns a string  """
        concern = Skin_Concern.objects.create(
            name='test_concern',
            friendly_name="Test Concern"
            )
        self.assertEqual(str(concern.name), 'test_concern')
        self.assertEqual(str(concern.friendly_name), 'Test Concern')

    def test_brand(self):
        """ Test if the brand model returns a string  """
        brand = Brand.objects.create(
            name='brand',
            friendly_name="Brand"
            )
        self.assertEqual(str(brand.name), 'brand')
        self.assertEqual(str(brand.friendly_name), 'Brand')

    def test_product(self):
        """ Test if the product model returns a string """
        product = Product.objects.create(
            name='Test Name',
            description='test description',
            price='25.00',
            rating='4.6',
            ingredients_list='test ingredient list',
            line_number='1',
        )
        self.assertEqual(str(product), 'Test Name')
