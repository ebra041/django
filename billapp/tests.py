from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.urls import reverse

from .models import Bill, Food, BillOrders
from django.conf import settings
from importlib import import_module


# Create your tests here.
class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Food.objects.create(foodname='cola', quantity = 3, cost = 5000, description='django')
        Bill.objects.create(employee=User.objects.get(username='admin'), client='ibrahim')
        BillOrders.objects.create(order=Food.objects.get(foodname='cola'), bill = Bill.objects.get(id=1))
        
    def test_url_allowed_hosts(self):
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='127.0.0.1')
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_url(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_html(self):
        response = self.c.get('/')
        html = response.content.decode('utf8')
        self.assertIn('<title>\nHome Page\n</title>', html)
        self.assertTrue(html.startswith('\n<!doctype html>\n'))
        self.assertEqual(response.status_code, 200)
        
        
class TestModel(TestCase):

    def setUp(self):
        self.client = Client()
        response = self.client.post("/login/", {"username": "admin", "password": "123"})
        self.assertEqual(response.status_code, 200)
        self.factory = RequestFactory()
        User.objects.create(username='admin', password='123')
        self.data1 = Food.objects.create(foodname='cola', quantity = 3, cost = 5000, description='django')
        Bill.objects.create(employee=User.objects.get(username='admin'), client='ibrahim')
        BillOrders.objects.create(order=Food.objects.get(foodname='cola'), bill = Bill.objects.get(id=1))

    def test_food_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Food))
        self.assertEqual(str(data), 'cola')

    def test_food_url(self):
        data = self.data1
        response = self.client.post(
            reverse('food', args=[data.id]))
        self.assertEqual(response.status_code, 302)
        
class TestLogin(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='admin', password='123')
    def test_login_fail(self):
        login_url = reverse('login')
        data = {
            'form_data': {
            'username': 'admin',
            'password': '123',
                         }
        }
        response = self.client.post(login_url, data, format='json')
        self.assertEqual(response.status_code, 200)