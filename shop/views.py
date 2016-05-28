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

def add_books_and_genres():
    Book.objects.all().delete()
    Genre.objects.all().delete()

    new_genre1 = Genre(genre='Научная фантастика')
    new_genre1.save()
    new_genre2 = Genre(genre='Детектив')
    new_genre2.save()
    new_genre3 = Genre(genre='Драма')
    new_genre3.save()
    new_genre4 = Genre(genre='Роман')
    new_genre4.save()
    new_genre5 = Genre(genre='Антиутопия')
    new_genre5.save()
    new_genre6 = Genre(genre='Фэнтези')
    new_genre6.save()
    new_genre7 = Genre(genre='Повесть')
    new_genre7.save()
    new_genre8 = Genre(genre='Триллер')
    new_genre8.save()
    new_genre9 = Genre(genre='Сказка')
    new_genre9.save()
    new_genre10 = Genre(genre='Приключения')
    new_genre10.save()


    new_book = Book(title='Игра престолов', author='Джордж Р. Р. Мартин', price=320, rating=9.2, audio=False)
    new_book.save()
    new_book.add_genres()
    new_book.genres.add(new_genre6)
    new_book.genres.add(new_genre4)
    new_book.save()
    new_book = Book(title='451 градус по Фаренгейту', author='Брэдбери Рэй Дуглас', price=390, rating=8.7, audio=False)
    new_book.save()
    new_book.add_genres()
    new_book.genres.add(new_genre1)
    new_book.genres.add(new_genre5)
    new_book.genres.add(new_genre4)
    new_book.save()
    new_book = Book(title='Портрет Дориана Грея', author='Оскар Уайльд', price=280, rating=8.6, audio=False)
    new_book.save()
    new_book.add_genres()
    new_book.genres.add(new_genre4)
    new_book.save()
    new_book = Book(title='Великий Гэтсби', author='Фрэнсис Скотт Фицджеральд', price=470, rating=8.3, audio=False)
    new_book.save()
    new_book.add_genres()
    new_book.genres.add(new_genre4)
    new_book.save()
    new_book = Book(title='Собака Баскервилей', author='Артур Конан Дойл', price=440, rating=9.1, audio=False)
    new_book.save()
    new_book.add_genres()
    new_book.genres.add(new_genre2)
    new_book.genres.add(new_genre7)
    new_book.save()
    new_book = Book(title='Зелёная миля', author='Стивен Кинг', price=390, rating=9.4, audio=False)
    new_book.save()
    new_book.add_genres()
    new_book.genres.add(new_genre8)
    new_book.genres.add(new_genre3)
    new_book.genres.add(new_genre4)
    new_book.save()
    new_book = Book(title='Чарли и шоколадная фабрика', author='Роальд Даль', price=510, rating=8.8, audio=False)
    new_book.save()
    new_book.add_genres()
    new_book.genres.add(new_genre9)
    new_book.genres.add(new_genre7)
    new_book.save()
    new_book = Book(title='Приключения Тома Сойера', author='Марк Твен', price=420, rating=8.8, audio=False)
    new_book.save()
    new_book.add_genres()
    new_book.genres.add(new_genre4)
    new_book.genres.add(new_genre10)
    new_book.save()
    new_book = Book(title='Алиса в Стране чудес', author='Льюис Кэрролл', price=380, rating=8.7, audio=False)
    new_book.save()
    new_book.add_genres()
    new_book.genres.add(new_genre9)
    new_book.save()
    new_book = Book(title='Ночной администратор', author='Джон ле Карре', price=280, rating=7.6, audio=False)
    new_book.save()
    new_book.add_genres()
    new_book.genres.add(new_genre2)
    new_book.genres.add(new_genre3)
    new_book.save()


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
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('login')
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password_again = request.POST.get('password_again')
            if password != password_again:
                return render(request, 'shop/reg_page.html', {
                    'error': 'Пароли не совпадают'
                })
            
            # Create User
            new_user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
            friend_id = request.POST.get('friend_id')
            if friend_id != '':
                new_user.friend_id = friend_id
            new_user.save()

            # Copy User to Customer
            new_customer = Customer(user=new_user)
            new_customer.save()

            if 'token' in request.session:
                token = request.session['token']
                order = Order.objects.get(token=token)
                order.customer_id = Customer.objects.get(user=new_user)
                order.save()

            return HttpResponseRedirect('/accounts/profile')
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
        order = Order.objects.get(customer_id=customer)
        return order.token, request
    
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
    customer = Customer.objects.get(user=request.user)
    print(buying)

    books = []
    for b in buying:
        books.append(b.book_id)
    
    return render(request, 'shop/bag_page.html', {
        'books': books,
        'sum': order.total_price,
        'bonus': order.total_price // 20,
        'avaliable_bonus': customer.bonus,
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