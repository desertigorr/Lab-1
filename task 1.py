# Task 1 - Count

import csv

with open('books.csv', 'r', encoding='cp1251') as f:
    table = csv.reader(f, delimiter=';')
    print('Всего записей: ' + str(len(list(table))))


