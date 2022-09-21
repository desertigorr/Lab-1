# Task 4 - Random book link generator
# У меня пятый вариант, доп. ограничения не предусмотрены

import csv
import random

row_count = 0

file = open('result.txt', 'w', encoding='utf-16')

# Вычисляем кол-во строк в таблице и сохраняем значение в переменную
with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')
    
    for i in table:
        row_count += 1

with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')

    # Создаем массив для рандомных ID
    id_list = []

    # Сюда будем складировать записи исходя из их ID
    book_list = []

    # Наполняем массив с ID
    for i in range(20):
        id_list.append(random.randint(0, row_count))

    # Преобразованная таблица в виде массива
    table_list = list(table)

    count = 0

    for i in id_list:
        count += 1
        table_row = table_list[i]

        author = str(table_row[3])
        if author == '':
            author = 'Автор незивестен'
        
        output = str(count) + '. ' + author + '. ' + table_row[1] + ' - ' + table_row[6][6:10] + '\n'
        file.write(output)
    
file.close()









