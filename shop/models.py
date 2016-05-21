from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Customer(User):
    friend_id = models.ForeignKey('self', on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    bonus = models.FloatField()


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField()
    bonus_added = models.FloatField()
    bonus_used = models.FloatField()
    promo_code = models.CharField(max_length=100)


class Genre(models.Model):
    genre = models.CharField(max_length=100)


class Language(models.Model):
    language = models.CharField(max_length=100)


class Qoute(models.Model):
    qoute = models.TextField()


class Comment(models.Model):
    comment = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover_root = models.CharField(max_length=100)
    price = models.FloatField()
    genres = models.ManyToManyField(Genre)
    description = models.TextField()
    rating = models.FloatField()
    languages = models.ManyToManyField(Language)
    audio = models.BooleanField()
    qoutes = models.ManyToManyField(Qoute)
    comments = models.ManyToManyField(Comment)


class Buying(models.Model):
    buying_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()


