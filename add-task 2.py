# Additional task 2 - 20 bestsellers

import csv

# Сортировка вставками (использовал готовый код)

def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:

            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = cursor

    return arr

with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')

    # Создаем массив
    books_list = []

    for row in table:

        # Отметаем строки, состоящие не из чисел
        if row[8].isdigit():
            books_list.append((int(row[8]), row[1], row[3]))

    # Сортируем массив
    # Примечание: books_list представляет собой массив, состоящий из сетов
    # Первый элемент сета - популярность книги (число), что делает возможным сортировку такой конструкции

    books_sorted = insertion_sort(books_list)

    for i in range(len(books_sorted)-1, len(books_sorted)-25, -1):
        book = books_sorted[i]
        print(str(book[2]) + ' - ' + str(book[1]) + '. Количество выдач: ' + str(book[0]))


