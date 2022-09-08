from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from basket.session import BasketSession
from store.models import Book


def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = BasketSession(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookId'))
        book = get_object_or_404(Book, id=book_id)
        basket.add(book=book)
        response = JsonResponse({'test': 'data'})
        return response
