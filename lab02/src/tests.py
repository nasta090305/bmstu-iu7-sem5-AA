import numpy as np
from funcs import *
from random import randint


def are_four_mtx_equal(c1, c2, c3, c4, n, m):
    for i in range(n):
        for j in range(m):
            if c1[i][j] != c2[i][j] or c1[i][j] != c3[i][j] or c1[i][j] != c4[i][j]:
                return False
    return True


def create_random_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = randint(-100, 100)
    return matrix


start, end = 3, 7
for i in range(start, end):
    for j in range(start, end):
        for k in range(start, end):
            A = create_random_matrix(i, j)
            B = create_random_matrix(j, k)
            C1 = standart_mtx_mul(A, B)
            C2 = winograd_mtx_mul(A, B)
            C3 = opt_winograd_mtx_mul(A, B)
            C4 = np.dot(A, B)
            if not are_four_mtx_equal(C1, C2, C3, C4, i, k):
                print("i =", i,  ", j =", j, ", k =", k, "ERROR")