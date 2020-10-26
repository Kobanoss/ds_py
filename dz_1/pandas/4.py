"""
Создайте датафрейм authors_stat на основе информации из authors_price.
В датафрейме authors_stat должны быть четыре столбца:
    author_name, min_price, max_price и mean_price,
    в которых должны содержаться соответственно имя автора,минимальная,
        максимальная и средняя цена на книги этого автора.
"""
import pandas as pd

# Выгрузка с предыдущего задания

authors = pd.DataFrame({'author_id': [1, 2, 3], 'author_name': ['Тургенев', 'Чехов', 'Островский']})

print(authors)

books = pd.DataFrame({'author_id':   [1, 1, 1, 2, 2, 3, 3],
                     'book_title':  ['Отцы и дети', 'Рудин', 'Дворянское гнездо',
                                    'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price':       [450, 300, 350, 500, 450, 370, 290] })

print(books)

authors_price = pd.merge(left = authors, right=books, left_on='author_id', right_on='author_id')

print(authors_price)


top5 = authors_price.sort_values('price', ascending=False)[0:5]

print(top5)

# Выгрузка с предыдущего задания


authors_stat_tmp = authors_price.set_index(['author_name', 'price'])
authors_stat_tmp.sort_index()
authors_stat = pd.DataFrame() # TODO

print(authors_stat)