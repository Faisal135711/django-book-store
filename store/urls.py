from django.urls import path

from store import views

app_name = 'store'
urlpatterns = [
    path("", views.all_books, name='all_books'),
    path("item/<slug:slug>/", views.book_detail, name='book_detail'),
    path("search/<slug:slug>/", views.category_detail, name='category_detail'),
]
