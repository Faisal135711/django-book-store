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
        book_id = book.id
        if book_id not in self.basket:
            self.basket[book_id] = {'price': str(book.price), 'qty': int(qty)}
        self.session.modified = True


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