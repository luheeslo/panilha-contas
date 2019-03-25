import json

from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Register
from .serializers import RegisterSerializer


client = Client()


class TestLists(TestCase):

    """Test case docstring."""

    def setUp(self):
        self.valid_payload = {
            'email': 'test@test.com',
            'password': 'mypassword',
        }
        User.objects.create_user('usertest', 'test@test.com', 'mypassword')
        client.post(reverse('myauth:login'),
                    data=json.dumps(self.valid_payload),
                    content_type='application/json')
        Register.objects.create(name='Ventilador', amount=-149.0)
        Register.objects.create(name='Feira do mês', amount=-250.0)
        Register.objects.create(name='Pagamento do job', amount=4000.0)

    def test_register_list(self):
        response = client.get(reverse('lists:registers'))
        registers = Register.objects.all()
        serializer = RegisterSerializer(registers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
