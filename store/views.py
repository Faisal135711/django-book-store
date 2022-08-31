from django.shortcuts import render

from store.models import Category, Book 

# Create your views here.
def all_books(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})