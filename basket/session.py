class BasketSession():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, book):
        book_id = book.id
        if book_id not in self.basket:
            self.basket[book_id] = {'price': float(book.price)}
        self.session.modified = True