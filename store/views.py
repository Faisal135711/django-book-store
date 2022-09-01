from django.shortcuts import render

from store.models import Category, Book 

def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_books(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})