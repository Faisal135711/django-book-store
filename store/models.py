from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class BookManager(models.Manager):
    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse("store:category_detail", args=[self.slug])

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='book_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    books = BookManager()

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("store:book_detail", args=[self.slug])
    
    def __str__(self):
        return self.title