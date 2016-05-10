from django.contrib import admin

from .models import Customer, Order, Book, Genre, Buying

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Buying)
