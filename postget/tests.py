from django.test import TestCase
from .models import User

# Create your tests here.
class TestModels(TestCase):
    def test_slug(self):
        user1 = User.objects.create(fname='ibrahim', sname ='zomorod', password='123')
        self.assertEquals(user1.slug, 'ibrahimzomorod')