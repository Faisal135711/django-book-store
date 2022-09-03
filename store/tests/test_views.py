from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Book, Category
from store.views import all_books

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
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_book_detail_url(self):
        response = self.client.get(reverse('store:book_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.client.get(reverse('store:category_detail', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_books(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get("/item/django-beginners")
        response = all_books(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
