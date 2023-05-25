from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import MenuItem

class MenuItemTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = MenuItem.objects.create(title="Pasta", price=50, inventory=120)
    def test_getall(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("LittleLemonAPI:menu-items"))
        self.assertContains(response,self.item1.title)
        self.assertContains(response,self.item1.price)
        self.assertContains(response,self.item1.inventory)
        self.assertContains(response,self.item2.title)
        self.assertContains(response,self.item2.price)
        self.assertContains(response,self.item2.inventory)