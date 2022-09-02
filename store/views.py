from django.shortcuts import render, get_object_or_404

from store.models import Category, Book 

def categories(request):
    return {
        'categories': Category.objects.all()
    }


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

