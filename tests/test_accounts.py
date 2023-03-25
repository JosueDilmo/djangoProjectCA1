from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# CA3 - TEST CASE
# TESTING BUILT-IN ACCOUNTS APP

class AccountsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )

    def test_login(self):
        # Make a GET request to the login page
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # Make a POST request to the login page with correct credentials
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post(reverse('login'), data)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_logout(self):
        # Log the user in
        self.client.login(username='testuser', password='testpass123')

        # Make a GET request to the logout page
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_registration(self):
        # Make a GET request to the registration page
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

        # Make a POST request to the registration page with valid data
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpass123',
            'password2': 'newpass123',
        }
        response = self.client.post(reverse('signup'), data)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

