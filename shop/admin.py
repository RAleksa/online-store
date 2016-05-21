from django.contrib import admin

from .models import Customer, Order, Genre, Language, Qoute, Comment, Book, Buying

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Qoute)
admin.site.register(Comment)
admin.site.register(Book)
admin.site.register(Buying)
