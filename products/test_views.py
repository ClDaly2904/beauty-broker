from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Product, Product_Category, Skin_Concern


class ProductDetailTestViews(TestCase):
    """ Test for the views in Product app """

    def setUp(self):
        cleansers = Product_Category.objects.create(
            name='cleansers',
            friendly_name='Cleansers',
        )

        oily_skin = Skin_Concern.objects.create(
            name='oily_skin',
            friendly_name='Oily Skin',
        )

        self.product = Product.objects.create(
            product_type=cleansers,
            skin_type=oily_skin,
            name='glossier product',
            description='test description',
            price='25.00',
            rating='4.6',
            ingredients_list='test ingredient list',
            line_number='1',
        )

        self.superuser = User.objects.create_superuser(
            'super', 'super@email.com', 'superpassword'
        )

        self.user = User.objects.create_user(
            'testuser', 'test@email.com', 'testpassword'
        )

    def test_products_page(self):
        """ Test products page load """

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail(self):
        """ Test product detail page load """

        response = self.client.get(reverse(
            'product_detail', args=[self.product.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product(self):
        """ Test add product page loads """

        self.client.login(username='super', password='superpassword')
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_edit_product(self):
        """ Test if edit product page loads """

        self.client.login(username='super', password='superpassword')
        response = self.client.get(reverse(
            'edit_product', args=[self.product.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_delete_product(self):
        """ Test if delete product page loads """

        self.client.login(username='super', password='superpassword')
        response = self.client.get(reverse(
            'delete_product', args=[self.product.pk])
        )
        self.assertEqual(response.status_code, 200)

    # SUPERUSERS
    def test_only_superuser_can_add(self):
        """ Test only superusers can add products """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/products/add/', follow=True)
        self.assertEqual(response.status_code, 200)
        # check error message
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            "Sorry, you're not authorised to do that." in message.message
        )

    def test_only_superuser_can_edit(self):
        """ Test only superusers can edit products """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse(
            'edit_product', args=[self.product.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            "Sorry, you're not authorised to do that." in message.message
        )

    def test_only_superuser_delete_edit(self):
        """ Test only superusers can access delete products """

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse(
            'delete_product', args=[self.product.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            "Sorry, you're not authorised to do that." in message.message
        )
