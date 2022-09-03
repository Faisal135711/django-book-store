from django.shortcuts import get_object_or_404, render

from store.models import Book, Category


def all_books(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug, in_stock=True)
    return render(request, 'store/books/detail.html', {'book': book})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.filter(category=category)
    return render(request, 'store/books/category.html', {'category': category, 'books': books})

