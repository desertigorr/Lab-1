# Task 4 - Random book link generator
# У меня пятый вариант, доп. ограничения не предусмотрены


import csv
import random


with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')

    # Создаем список рандомных ID в виде массива
    id_list = []
    # Сюда будем складировать записи исходя из их ID
    book_list = []
    # Создаем массив с ID
    for i in range(20):
        id_list.append(random.randint(0, 9410))

    # Сортируем, чтобы наполнить book_list за один проход по таблице
    id_list = sorted(id_list)

    id = 0
    count = 0

    for row in table:
        if id == id_list[0] and count < 19:
            book_list.append(row)
            id_list.pop(0)
            id += 1
            count += 1
        else:
            id += 1

    # Выводим 20 рандомных записей
    for i in range(len(book_list)):
        print(str(book_list[i][3]) + '. '+str(book_list[i][1]) + ' - ' + str(book_list[i][6][6:10]))








