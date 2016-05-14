from django.contrib import admin

from .models import Customer, Order, Genre, Language, Book, Buying

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Buying)
