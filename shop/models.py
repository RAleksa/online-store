from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import random


class Customer(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(null=True, blank=True)
    bonus = models.IntegerField(default=0)


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField()
    date_bought = models.DateTimeField(null=True, blank=True)
    total_price = models.IntegerField(default=0)
    bonus_added = models.FloatField(default=0)
    bonus_used = models.FloatField(default=0)
    promo_code = models.CharField(max_length=100, null=True, blank=True)

    def generate_token():
        char = [chr(i) for i in range(ord('a'), ord('z'))] + [chr(i) for i in range(ord('A'), ord('Z'))] + [str(i) for i in range(10)]
        return ''.join([random.choice(char) for i in range(40)])

    token = models.CharField(max_length=40, default=generate_token())


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
    price = models.IntegerField()
    genres = models.ManyToManyField(Genre, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField()
    cover_root = models.CharField(max_length=100, null=True, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    audio = models.BooleanField()
    qoutes = models.ManyToManyField(Qoute, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)

    def add_genres(self, genres):
        for genre in genres:
            new_genre = Genre.objects.filter(genre=genre)

            if not new_genre:
                return None

            self.genres.add(new_genre[0])

        return 'OK'


class Buying(models.Model):
    buying_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


