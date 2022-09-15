from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Book


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Book.objects.create(category_id=1,
                            title='django beginners',
                            created_by_id=1,
                            slug='django-beginners',
                            price='20.00',
                            image='django')
        Book.objects.create(category_id=1,
                            title='django intermediate',
                            created_by_id=1,
                            slug='django-beginners',
                            price='20.00',
                            image='django')
        Book.objects.create(category_id=1,
                            title='django advanced',
                            created_by_id=1,
                            slug='django-beginners',
                            price='20.00',
                            image='django')
        self.client.post(reverse('basket:basket_add'), {'bookId': 1, 'bookQty': 1,
                                                        'action': 'post'})
        self.client.post(reverse('basket:basket_add'), {'bookId': 2, 'bookQty': 2,
                                                        'action': 'post'})

    def test_basket_url(self):
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        response = self.client.post(reverse('basket:basket_add'),
                                            {'bookId': 3,
                                             'bookQty': 1,
                                             'action': 'post'},
                                            xhr=True)
        self.assertEqual(response.json(), {'qty': 4})

        response = self.client.post(reverse('basket:basket_add'),
                                            {'bookId': 2,
                                             'bookQty': 1,
                                             'action': 'post'},
                                            xhr=True)
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        response = self.client.post(reverse('basket:basket_delete'),
                                    {'bookId': 2,
                                     'action': 'post'},
                                    xhr=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '20.00'})

    def test_basket_update(self):
        response = self.client.post(reverse('basket:basket_update'),
                                    {'bookId': 2,
                                     'bookQty': 1,
                                     'action': 'post'},
                                    xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '40.00'})
