from funcs import *
import Levenshtein
from pyxdameraulevenshtein import damerau_levenshtein_distance


def menu():
    print()
    print("Меню:",
          "0) Завершить выполнение",
          "1) Вычислить расстояние Левенштейна итеративно",
          "2) Вычислить расстояние Левенштейна рекурсивно",
          "3) Вычислить расстояние Левенштейна рекурсивно с мемоизацией",
          "4) Вычислить расстояние Дамерау-Левенштейна итеративно",
          "5) Вычислить всё", sep='\n')
    try:
        return int(input("Введите номер команды: "))
    except Exception:
        print("Некорректный ввод")
        return -1


command = -1
while command != 0:
    command = menu()
    if command == 1:
        str1 = input("Введите первую строку: ")
        str2 = input("Введите вторую строку: ")
        res = matrix_levenstein(str1, str2)
        print("Расстояние Левенштейна =", res)
        print("Результат работы библиотечной функции =", Levenshtein.distance(str1, str2))
    elif command == 2:
        str1 = input("Введите первую строку: ")
        str2 = input("Введите вторую строку: ")
        res = recurs_levenstein(str1, str2)
        print("Расстояние Левенштейна =", res)
        print("Результат работы библиотечной функции =", Levenshtein.distance(str1, str2))
    elif command == 3:
        str1 = input("Введите первую строку: ")
        str2 = input("Введите вторую строку: ")
        res = memo_levenstein(str1, str2)
        print("Расстояние Левенштейна =", res)
        print("Результат работы библиотечной функции =", Levenshtein.distance(str1, str2))
    elif command == 4:
        str1 = input("Введите первую строку: ")
        str2 = input("Введите вторую строку: ")
        res = damerau_levenstein(str1, str2)
        print("Расстояние Дамерау-Левенштейна =", res)
        print("Результат работы библиотечной функции =", damerau_levenshtein_distance(str1, str2))
    elif command == 5:
        str1 = input("Введите первую строку: ")
        str2 = input("Введите вторую строку: ")
        print("Расстояние Левенштейна итеративно =", matrix_levenstein(str1, str2))
        print("Расстояние Левенштейна рекурсивно =", recurs_levenstein(str1, str2))
        print("Расстояние Левенштейна рекурсивно с мемоизацией =", memo_levenstein(str1, str2))
        print("Расстояние Левенштейна из библиотеки =", Levenshtein.distance(str1, str2))
        print("Расстояние Дамерау-Левенштейна =", damerau_levenstein(str1, str2))
        print("Расстояние Дамерау-Левенштейна из библиотеки =", damerau_levenshtein_distance(str1, str2))