# Task 3 - Search by author

import csv


with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')

    search = input('Введите имя автора: ')

    search = search.lower()
    print('Что удалось найти:')
    flag = 0
    for row in table:
        author = row[3].lower()
        if search in author:
            flag = 1
            print(row[3], '-', row[1])
    if flag == 0:
        print('Ничего не найдено')





