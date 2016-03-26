# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm

books = [
        {'id':0, 'name':'451 градус по Фаренгейту', 'author':'Брэдбери Рэй Дуглас', 'price':390, 'rating':8.7, 'rus':True, 'eng':True,
        'genre':['Научная фантастика', 'Антиутопия', 'Роман'], 'visible':True},
        {'id':1, 'name':'Портрет Дориана Грея', 'author':'Оскар Уайльд', 'price':280, 'rating':8.6, 'rus':True, 'eng':True,
        'genre':['Роман'], 'visible':True},
        {'id':2, 'name':'Великий Гэтсби', 'author':'Фрэнсис Скотт Фицджеральд', 'price':470, 'rating':8.3, 'rus':True, 'eng':True,
        'genre':['Роман'], 'visible':True},
        {'id':3, 'name':'Игра престолов', 'author':'Джордж Р. Р. Мартин', 'price':320, 'rating':9.2, 'rus':True, 'eng':True,
        'genre':['Фэнтези', 'Роман'], 'visible':True},
        {'id':4, 'name':'Собака Баскервилей', 'author':'Артур Конан Дойл', 'price':440, 'rating':9.1, 'rus':True, 'eng':True,
        'genre':['Детектив', 'Повесть'], 'visible':True},
        {'id':5, 'name':'Зелёная миля', 'author':'Стивен Кинг', 'price':390, 'rating':9.4, 'rus':True, 'eng':True,
        'genre':['Триллер', 'Драма', 'Роман'], 'visible':True},
        {'id':6, 'name':'Чарли и шоколадная фабрика', 'author':'Роальд Даль', 'price':510, 'rating':8.8, 'rus':True, 'eng':True,
        'genre':['Сказка', 'Повесть'], 'visible':True},
        {'id':7, 'name':'Приключения Тома Сойера', 'author':'Марк Твен', 'price':420, 'rating':8.8, 'rus':True, 'eng':True,
        'genre':['Приключения', 'Роман'], 'visible':True},
        {'id':8, 'name':'Алиса в Стране чудес', 'author':'Льюис Кэрролл', 'price':380, 'rating':8.7, 'rus':True, 'eng':True,
        'genre':['Сказка'], 'visible':True},
        {'id':9, 'name':'Ночной администратор', 'author':'Джон ле Карре', 'price':280, 'rating':7.6, 'rus':True, 'eng':True,
        'genre':['Детектив', 'Драма'], 'visible':True},
    ]

books.sort(key=lambda x: -x['rating'])

genres = [
    'Научная фантастика',
    'Детектив',
    'Драма',
    'Роман',
    'Антиутопия',
    'Фэнтези',
    'Повесть',
    'Триллер',
    'Сказка',
    'Приключения',
]

@csrf_exempt
def paypal_success(request):
    return HttpResponse("Money is mine. Thanks.")


@login_required
def paypal_pay(request):
    s = 0;
    for i in range(len(books)):
        s += books[i]['price']
    paypal_dict = {
        "business": "aoryabinina-facilitator@gmail.com",
        "amount": s,
        "currency_code": "RUB",
        "item_name": "products in shop",
        "invoice": "INV-00001",
        "notify_url": reverse('paypal-ipn'),
        "return_url": "http://127.0.0.1:8000/payment/success/",
        "cancel_return": "http://127.0.0.1:8000/payment/cart/",
        "custom": str(request.user.id),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        "form": form,
        "paypal_dict": paypal_dict,
        'auth': request.user.is_authenticated(),
    }
    return render(request, "shop/payment_page.html", context)

@login_required
def account_profile(request):
    first_name = request.user.first_name
    return render(request, 'shop/profile_page.html', {
        'first_name': request.user.first_name,
        'auth': request.user.is_authenticated(),
    })

def account_logout(request):
    logout(request)
    return redirect('/')

def main_page(request):
    for i in range(len(books)):
        books[i]['visible'] = True

    return render(request, 'shop/main_page.html', {
    	'books': books,
        'genres': genres,
        'auth': request.user.is_authenticated(),
    })

def genre_page(request, genre):
    for i in range(len(books)):
        books[i]['visible'] = True
    for i in range(len(books)):
        if genres[int(genre)] not in books[i]['genre']:
            books[i]['visible'] = False
    return render(request, 'shop/main_page.html', {
        'books': books,
        'genres': genres,
        'auth': request.user.is_authenticated(),
    })

def reg_page(request):
    return render(request, 'shop/reg_page.html', {
    })

def passrecovery_page(request):
    return render(request, 'shop/passrecovery_page.html', {
        'auth': request.user.is_authenticated(),
    })


def bag_page(request):
    s = 0;
    for i in range(len(books)):
        s += books[i]['price']
    return render(request, 'shop/bag_page.html', {
        'books': books,
        'sum': s,
        'bonus': s // 20,
        'avaliable_bonus': 450,
        'auth': request.user.is_authenticated(),
    })

def book_page(request, book_id):
    if int(book_id) >= len(books):
        return HttpResponseNotFound('<h2>Упс! Такой книги нет :(  Попробуйте другую.</h2>')
    id = -1
    for i in range(len(books)):
        if books[i]['id'] == int(book_id):
            id = i
            break

    return render(request, 'shop/book_page.html', {
    	"book_id": book_id,
        "book": books[id],
        'auth': request.user.is_authenticated(),
    })

def addtobag(request):
    return HttpResponse("Добавлено")