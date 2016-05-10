from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    login = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    friend_id = models.ForeignKey('self', on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    bonus = models.FloatField()


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField()
    bonus_added = models.FloatField()
    bonus_used = models.FloatField()
    promo_code = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover_root = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    rating = models.FloatField()
    language = models.CharField(max_length=100)
    audio = models.BooleanField()
    qoutes = models.TextField()
    comments = models.TextField()


class Genre(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)


class Buying(models.Model):
    buying_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()


