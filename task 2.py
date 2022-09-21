# Task 2 - Count > 30

import csv

with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')

    c = 0
    for row in table:
        if len(row[1]) > 30:
            c += 1
            
    print('Записей с длиной названия > 30 символов: ', c)



