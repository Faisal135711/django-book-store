from store.models import Book

from decimal import Decimal

class BasketSession():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket


    def add(self, book, qty):
        book_id = str(book.id)
        if book_id not in self.basket:
            self.basket[book_id] = {'price': str(book.price), 'qty': int(qty)}
        else:
            self.basket[book_id]['qty'] = int(qty)

        self.save()


    def delete(self, book):
        book_id = str(book)
        if book_id in self.basket:
            del self.basket[book_id]
            self.save()


    def update(self, book, qty):
        book_id = str(book)
        if book_id in self.basket:
            self.basket[book_id]['qty'] = qty
        self.save()


    def __iter__(self):
        book_ids = self.basket.keys()
        books = Book.books.filter(id__in=book_ids)
        basket = self.basket.copy()

        for book in books:
            basket[str(book.id)]['book'] = book

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())


    def save(self):
        self.session.modified = True
