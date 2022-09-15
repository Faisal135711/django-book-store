from unittest import skip

from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Book, Category
from store.views import book_all

# Create your tests here.
# @skip('demonstrating skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass

class TestViewResponses(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        Book.objects.create(category_id=1, 
                                         title='django beginners', 
                                         created_by_id=1,
                                         slug='django-beginners',
                                         price='20.00',
                                         image='django')


    def test_url_allowed_hosts(self):
        response = self.client.get("/", HTTP_HOST='myaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.client.get("/", HTTP_HOST='mydomain.com')
        self.assertEqual(response.status_code, 200)
        

    def test_book_detail_url(self):
        response = self.client.get(reverse('store:book_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)


    def test_category_detail_url(self):
        response = self.client.get(reverse('store:category_detail', args=['django']))
        self.assertEqual(response.status_code, 200)
        

    def test_homepage_html(self):
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = book_all(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>Book Store</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    
