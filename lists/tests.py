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

    def test_register_list_order_by_name(self):
        response = client.get(reverse('lists:registers'), {'order_by': 'name'})
        registers = Register.objects.all().order_by("name")
        serializer = RegisterSerializer(registers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_list_order_by_amount(self):
        response = client.get(reverse('lists:registers'), {'order_by': 'amount'})
        registers = Register.objects.all().order_by("amount")
        serializer = RegisterSerializer(registers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_list_order_by_name_sort_by_desc(self):
        response = client.get(reverse('lists:registers'),
                              {'order_by': 'name', 'sort_by': 'd'})
        registers = Register.objects.all().order_by("-name")
        serializer = RegisterSerializer(registers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_list_order_by_amount_sort_by_desc(self):
        response = client.get(reverse('lists:registers'),
                              {'order_by': 'amount', 'sort_by': 'd'})
        registers = Register.objects.all().order_by("-amount")
        serializer = RegisterSerializer(registers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCreateRegister(TestCase):

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

    def test_create_register_input(self):
        response = client.post(reverse('lists:create_register'),
                               data="type=1&name=Teste&amount=200.00",
                               content_type="application/x-www-form-urlencoded")
        register = Register.objects.filter(name="Teste").first()
        serializer = RegisterSerializer(register)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 201)

    def test_create_register_output(self):
        response = client.post(reverse('lists:create_register'),
                               data="type=2&name=Teste&amount=200.00",
                               content_type="application/x-www-form-urlencoded")
        register = Register.objects.filter(name="Teste").first()
        serializer = RegisterSerializer(register)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.data['amount'], '-200.00')
        self.assertEqual(response.status_code, 201)
