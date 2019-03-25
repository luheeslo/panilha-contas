import json

from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


client = Client()


class TestAuth(TestCase):

    """Test module for login and logout"""

    def setUp(self):
        self.valid_payload = {
            'email': 'test@test.com',
            'password': 'mypassword',
        }
        User.objects.create_user('usertest', 'test@test.com', 'mypassword')

    def test_login_ok(self):
        response = client.post(reverse('myauth:login'),
                               data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_incorrect_user(self):
        self.valid_payload['email'] = 'otherusertest@test.com'
        response = client.post(reverse('myauth:login'),
                               data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_incorrect_password(self):
        self.valid_payload['password'] = 'otherpassword'
        response = client.post(reverse('myauth:login'),
                               data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_logout(self):
        response = client.post(reverse('myauth:login'),
                               data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = client.post(reverse('myauth:logout'))
        self.assertEqual(response.status_code, 200)

    def test_logout_auth_not_provided(self):
        response = client.post(reverse('myauth:logout'))
        self.assertEqual(response.status_code, 403)
