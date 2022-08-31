from django.urls import path 

from store import views

app_name = 'store'
urlpatterns = [
    path("", views.all_books, name='all_books'),
]
