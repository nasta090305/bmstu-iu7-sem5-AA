from funcs import *


def menu():
    print()
    print("Меню:\n",
          "0) Завершить выполнение\n",
          "1) Вычислить результат умножения матриц стандартным методом\n",
          "2) Вычислить результат умножения матриц алгоритмом Винограда\n",
          "3) Вычислить результат умножения матриц алгоритмом Винограда с оптимизациями\n",
          "4) Вычислить всё\n")
    try:
        return int(input("Введите номер команды: "))
    except Exception:
        print("Некорректный ввод")
        return -1


command = -1
while command != 0:
    command = menu()
    if command == 1:
        print("Введите первую матрицу:")
        matrix1 = scan_matrix()
        if not matrix1:
            print("Ошибка ввода")
            continue
        print("Введите вторую матрицу:")
        matrix2 = scan_matrix()
        if not matrix2:
            print("Ошибка ввода")
            continue
        res_matrix = standart_mtx_mul(matrix1, matrix2)
        if not res_matrix:
            print("Ошибка умножения")
            continue
        print("Полученная матрица:")
        print_matrix(res_matrix)
    elif command == 2:
        print("Введите первую матрицу:")
        matrix1 = scan_matrix()
        if not matrix1:
            print("Ошибка ввода")
            continue
        print("Введите вторую матрицу:")
        matrix2 = scan_matrix()
        if not matrix2:
            print("Ошибка ввода")
            continue
        res_matrix = winograd_mtx_mul(matrix1, matrix2)
        if not res_matrix:
            print("Ошибка умножения")
            continue
        print("Полученная матрица:")
        print_matrix(res_matrix)
    elif command == 3:
        print("Введите первую матрицу:")
        matrix1 = scan_matrix()
        if not matrix1:
            print("Ошибка ввода")
            continue
        print("Введите вторую матрицу:")
        matrix2 = scan_matrix()
        if not matrix2:
            print("Ошибка ввода")
            continue
        res_matrix = opt_winograd_mtx_mul(matrix1, matrix2)
        if not res_matrix:
            print("Ошибка умножения")
            continue
        print("Полученная матрица:")
        print_matrix(res_matrix)
    elif command == 4:
        print("Введите первую матрицу:")
        matrix1 = scan_matrix()
        if not matrix1:
            print("Ошибка ввода")
            continue
        print("Введите вторую матрицу:")
        matrix2 = scan_matrix()
        if not matrix2:
            print("Ошибка ввода")
            continue
        res_matrix1 = standart_mtx_mul(matrix1, matrix2)
        res_matrix2 = winograd_mtx_mul(matrix1, matrix2)
        res_matrix3 = opt_winograd_mtx_mul(matrix1, matrix2)
        if not res_matrix1 or not res_matrix2 or not res_matrix3:
            print("Ошибка умножения")
            continue
        print("Полученные матрицы:")
        print("Стандартный алгоритм:")
        print_matrix(res_matrix1)
        print("Алгоритм Винограда:")
        print_matrix(res_matrix2)
        print("Алгоритм Винограда с оптимизациями:")
        print_matrix(res_matrix3)