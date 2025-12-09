from cmp_counter import *
from random import randint


def menu():
    print()
    print("Меню:")
    print("0) Завершить выполнение")
    print("1) Сгенерировать случайный массив заданной длины")
    print("2) Найти элемент в массиве перебором")
    print("3) Найти элемент в массиве бинарным поиском")
    try:
        return int(input("Введите номер команды: "))
    except Exception:
        print("Некорректный ввод")
        return -1


def generate_random_array(n):
    arr = []
    for i in range(n):
        arr.append(randint(-1000, 1000))
    return arr


def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()


command = -1
arr = []
while command != 0:
    command = menu()
    print()
    if command == 1:
        try:
            n = int(input("Введите размер массива: "))
            if n < 1:
                print("Неверный ввод")
                continue
        except:
            print("Неверный ввод")
            continue
        arr = generate_random_array(n)
        print("Сгенерированный массив:")
        print_array(arr)
    elif command == 2:
        if len(arr) == 0:
            print("Массив не сгенерирован")
            continue
        try:
            elem = int(input("Введите искомый элемент: "))
        except:
            print("Неверный ввод")
            continue
        res, cmp = linear_search(arr, elem)
        if res == -1:
            print(f"Элемент {elem} не найден")
        else:
            print(f"Индекс элемента {elem} равен {res}")
        print(cmp, "сравнений")
    elif command == 3:
        if len(arr) == 0:
            print("Массив не сгенерирован")
            continue
        try:
            elem = int(input("Введите искомый элемент: "))
        except:
            print("Неверный ввод")
            continue
        res, cmp = bin_search(arr, elem)
        if res == -1:
            print(f"Элемент {elem} не найден")
        else:
            print(f"Индекс элемента {elem} равен {res}")
        print(cmp, "сравнений")
