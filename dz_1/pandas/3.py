"""
Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.
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

# Выгрузка с предыдущего задания

top5 = authors_price.sort_values('price', ascending=False)[0:5]

print(top5)