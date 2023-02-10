from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from checkout.models import Order
from profiles.models import UserProfile


class TestProfilesViews(TestCase):
    """ Tests for profiles app views """

    def setUp(self):
        """ Set up user and object for profile views """

        testuser = User.objects.create_user(
            username='test_username',
            password='test',
            email='testuser@email.com'
        )
        testuser.save()

        Order.objects.create(
            order_number='1234567890',
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Test User',
            email='testuser@email.com',
            phone_number='12345678',
            country='GB',
            postcode='12345',
            town_or_city='Any City',
            street_address1='Test Street',
            county='Test County',
        )

    def tearDown(self):
        """ Test delete test user and order """

        User.objects.all().delete()
        Order.objects.all().delete()

    def test_get_profile(self):
        """ Test user can access their profile page via get """

        self.client.login(username='test_username', password='test')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_post_profile(self):
        """ Test user can access their profile page via post """

        self.client.login(username='test_username', password='test')
        response = self.client.post('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_get_order_detail(self):
        """ Test user can access their order history """

        self.client.login(username='test_username', password='test')
        testuser = User.objects.get(username='test_username')
        order = Order.objects.get(email=testuser.email)
        response = self.client.get('/profile/order_history/' +
                                   order.order_number)
        self.assertEqual(response.status_code, 200)
        # check upate message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         f'This is a past confirmation for order number'
                         f' {order.order_number}.\n'
                         'Please check your email inbox for the '
                         'order confirmation\n'
                         'sent on the day.')
