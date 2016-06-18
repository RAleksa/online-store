# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm

from .models import Customer, Order, Genre, Language, Qoute, Comment, Book, Buying
from django.utils import timezone

from django.contrib.auth.models import User
from django.http import JsonResponse

from django.core.cache import cache

BONUS_FOR_THE_ORDER = 0.05

@csrf_exempt
def paypal_success(request):
    return HttpResponse("Money is mine. Thanks.")

@login_required
def paypal_pay(request):
    s = 543
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
    customer = Customer.objects.filter(user=request.user)

    if not customer:
        customer = Customer(user=request.user)
        customer.save()
    else:
        customer = customer[0]

    return render(request, 'shop/profile_page.html', {
        'login': request.user.username,
        'name': request.user.first_name,
        'email': request.user.email,
        'special_id': customer.special_id,
        'bonus': customer.bonus,
        'auth': request.user.is_authenticated(),
    })


def account_logout(request):
    logout(request)
    return redirect('/')


def account_login(request):
    username = request.POST.get('login')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponseNotFound('<h2>Ошибка авторизации :(</h2>')
    else:
        return HttpResponseNotFound('<h2>Не удалось авторизоваться :(  Проверьте логин и пароль</h2>')


def main_page(request):
    books = cache.get_or_set('books', Book.objects.all(), 10)
    genres = Genre.objects.all()

    book_genres = []
    for book in books:
        book_genres.append(books[0].genres.all())

    return render(request, 'shop/main_page.html', {
        'books': books,
        'genres': genres,
        'auth': request.user.is_authenticated(),
    })


def genre_page(request, genre_id):
    books_all = Book.objects.all()
    genres = Genre.objects.all()

    genre = Genre.objects.filter(id=genre_id)
    if not genre:
        return HttpResponseNotFound('<h2>Жанр не найден :(</h2>')

    books = []
    for book in books_all:
        if genre[0] in book.genres.all():
            books.append(book)

    return render(request, 'shop/main_page.html', {
        'books': books,
        'genres': genres,
        'auth': request.user.is_authenticated(),
    })


def reg_page(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_again = request.POST.get('password_again')
        if password != password_again:
            return render(request, 'shop/reg_page.html', {
                'error': 'Пароли не совпадают',
                'login': username,
                'first_name': first_name,
                'email': email,
            })

        # Check if this username and email is free
        if User.objects.filter(username=username):
            return render(request, 'shop/reg_page.html', {
                'error': 'Этот логин уже занят',
                'login': username,
                'first_name': first_name,
                'email': email,
            })
        if User.objects.filter(email=email):
            return render(request, 'shop/reg_page.html', {
                'error': 'На этот email уже зарегистрирован аккаунт',
                'login': username,
                'first_name': first_name,
                'email': email,
            })
        
        friend_id = request.POST.get('friend_id')
        if friend_id:
            friend = Customer.objects.filter(special_id=friend_id)
            if friend:
                # Add bonus to a friend
                friend[0].bonus += 20
                friend[0].save()

            else:
                return render(request, 'shop/reg_page.html', {
                    'error': 'Пользователя с таким ID у нас нет',
                    'login': username,
                    'first_name': first_name,
                    'email': email,
                })

        # Create User
        new_user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)

        friend = Customer.objects.filter(special_id=friend_id)
        if friend:
            new_user.friend_id = friend[0]
            
        date_of_birth = request.POST.get('date_of_birth')
        if date_of_birth:
            new_user.date_of_birth = date_of_birth

        new_user.save()

        # Log in
        user = authenticate(username=username, password=password)
        login(request, user)

        # Copy User to Customer
        new_customer = Customer(user=new_user)
        new_customer.save()

        if 'token' in request.session:
            token = request.session['token']
            order = Order.objects.get(token=token)
            order.customer_id = Customer.objects.get(user=new_user)
            order.save()

        return HttpResponseRedirect('/accounts/profile')
    elif request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return render(request, 'shop/reg_page.html', {
        })


def passrecovery_page(request):
    return render(request, 'shop/passrecovery_page.html', {
        'auth': request.user.is_authenticated(),
    })


def get_order(request):
    if request.user.is_authenticated():
        customer = Customer.objects.get(user=request.user)
        if 'token' in request.session:
            order = Order.objects.get(token=request.session['token'])
            order.customer_id = customer
            order.save()
            return order.token, request
        else:
            order = Order.objects.filter(customer_id=customer)
            if order:
                return order[0].token, request
            else:
                new_order = Order(customer_id=customer, date_added=timezone.now())
                new_order.save()
                return new_order.token, request
    
    if 'token' in request.session:
        return request.session['token'], request
    
    new_order = Order(date_added=timezone.now())
    new_order.save()
    request.session['token'] = new_order.token
    return new_order.token, request


def bag_page(request):
    token, request = get_order(request)

    print("token: " + token)

    order = Order.objects.get(token=token)
    buying = Buying.objects.filter(buying_id=order)

    customer = None
    if request.user.is_authenticated():
        customer = Customer.objects.get(user=request.user)
    # print(buying)

    books = []
    for b in buying:
        books.append(b.book_id)
    
    return render(request, 'shop/bag_page.html', {
        'books': books,
        'sum': order.total_price,
        'bonus': round(order.total_price * BONUS_FOR_THE_ORDER),
        'avaliable_bonus': customer.bonus if customer is not None else '',
        'auth': request.user.is_authenticated(),
    })


def book_page(request, book_id):
    book = Book.objects.filter(id=book_id)
    if not book:
        return HttpResponseNotFound('<h2>Книга не найдена :(</h2>')

    return render(request, 'shop/book_page.html', {
        'book': book[0],
        'book_genres': book[0].genres.all(),
        'auth': request.user.is_authenticated(),
    })


def addtobag(request):
    book_name = request.POST.get('book_name')

    token, request = get_order(request)
    order = Order.objects.get(token=token)

    book = Book.objects.filter(title=book_name)
    if not book:
        return HttpResponseNotFound('<h2>Упс! Такой книги нет :(  Попробуйте другую.</h2>')
    
    if not Buying.objects.filter(buying_id=order, book_id=book[0]):
        new_buying = Buying(buying_id=order, book_id=book[0])
        new_buying.save()
        order.total_price += book[0].price
        order.save()

    return HttpResponse("Добавлено")

def delfrombag(request):
    book_id = int(request.POST.get('book_id'))

    token, request = get_order(request)
    order = Order.objects.get(token=token)

    book = Book.objects.filter(id=book_id)
    if not book:
        return HttpResponseNotFound('<h2>Ошибка :(</h2>')

    Buying.objects.filter(buying_id=order, book_id=book[0]).delete()
    order.total_price -= book[0].price
    order.save()


    return JsonResponse({
        'total_price': order.total_price,
        'bonus': round(order.total_price * BONUS_FOR_THE_ORDER),
    })