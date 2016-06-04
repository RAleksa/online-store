def add_genres():
    Genre.objects.all().delete()

    new_genre = Genre(genre='Научная фантастика')
    new_genre.save()
    new_genre = Genre(genre='Детектив')
    new_genre.save()
    new_genre = Genre(genre='Драма')
    new_genre.save()
    new_genre = Genre(genre='Роман')
    new_genre.save()
    new_genre = Genre(genre='Антиутопия')
    new_genre.save()
    new_genre = Genre(genre='Фэнтези')
    new_genre.save()
    new_genre = Genre(genre='Повесть')
    new_genre.save()
    new_genre = Genre(genre='Триллер')
    new_genre.save()
    new_genre = Genre(genre='Сказка')
    new_genre.save()
    new_genre = Genre(genre='Приключения')
    new_genre.save()

def add_books():
    Book.objects.all().delete()

    new_book = Book(title='Игра престолов', author='Джордж Р. Р. Мартин', price=320, rating=9.2, audio=False)
    new_book.save()
    new_book.add_genres(['Фэнтези', 'Роман'])
    new_book.save()
    new_book = Book(title='451 градус по Фаренгейту', author='Брэдбери Рэй Дуглас', price=390, rating=8.7, audio=False)
    new_book.save()
    new_book.add_genres(['Научная фантастика', 'Антиутопия', 'Роман'])
    new_book.save()
    new_book = Book(title='Портрет Дориана Грея', author='Оскар Уайльд', price=280, rating=8.6, audio=False)
    new_book.save()
    new_book.add_genres(['Роман'])
    new_book.save()
    new_book = Book(title='Великий Гэтсби', author='Фрэнсис Скотт Фицджеральд', price=470, rating=8.3, audio=False)
    new_book.save()
    new_book.add_genres(['Роман'])
    new_book.save()
    new_book = Book(title='Собака Баскервилей', author='Артур Конан Дойл', price=440, rating=9.1, audio=False)
    new_book.save()
    new_book.add_genres(['Детектив', 'Повесть'])
    new_book.save()
    new_book = Book(title='Зелёная миля', author='Стивен Кинг', price=390, rating=9.4, audio=False)
    new_book.save()
    new_book.add_genres(['Триллер', 'Драма', 'Роман'])
    new_book.save()
    new_book = Book(title='Чарли и шоколадная фабрика', author='Роальд Даль', price=510, rating=8.8, audio=False)
    new_book.save()
    new_book.add_genres(['Сказка', 'Повесть'])
    new_book.save()
    new_book = Book(title='Приключения Тома Сойера', author='Марк Твен', price=420, rating=8.8, audio=False)
    new_book.save()
    new_book.add_genres(['Приключения', 'Роман'])
    new_book.save()
    new_book = Book(title='Алиса в Стране чудес', author='Льюис Кэрролл', price=380, rating=8.7, audio=False)
    new_book.save()
    new_book.add_genres(['Сказка'])
    new_book.save()
    new_book = Book(title='Ночной администратор', author='Джон ле Карре', price=280, rating=7.6, audio=False)
    new_book.save()
    new_book.add_genres(['Детектив', 'Драма'])
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