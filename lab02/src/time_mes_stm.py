from utime import ticks_us
from random import randint

def standart_mtx_mul(A, B):
    m, t = len(A), len(B)
    if t == 0 or m == 0:
        return None
    n, q = len(A[0]), len(B[0])
    if n != t:
        return None
    C = [[0] * q for i in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C


def winograd_mtx_mul(A, B):
    m, t = len(A), len(B)
    if t == 0 or m == 0:
        return None
    n, q = len(A[0]), len(B[0])
    if n != t:
        return None
    C = [[0] * q for i in range(m)]
    mulh = [0] * m
    mulv = [0] * q
    for i in range(m):
        for k in range(n // 2):
            mulh[i] = mulh[i] + A[i][2 * k] * A[i][2 * k + 1]
    for i in range(q):
        for k in range(n // 2):
            mulv[i] = mulv[i] + B[2 * k][i] * B[2 * k + 1][i]
    for i in range(m):
        for j in range(q):
            C[i][j] = - mulh[i] - mulv[j]
            for k in range(n // 2):
                C[i][j] = (C[i][j] + (A[i][2 * k] + B[2 * k + 1][j])
                           * (A[i][2 * k + 1] + B[2 * k][j]))
    if n % 2 != 0:
        for i in range(m):
            for j in range(q):
                C[i][j] = C[i][j] + A[i][n - 1] * B[n - 1][j]
    return C


def opt_winograd_mtx_mul(A, B):
    m, t = len(A), len(B)
    if t == 0 or m == 0:
        return None
    n, q = len(A[0]), len(B[0])
    if n != t:
        return None
    C = [[0] * q for i in range(m)]
    mulh = [0] * m
    mulv = [0] * q
    for i in range(m):
        for k in range(n // 2):
            mulh[i] -= A[i][2 * k] * A[i][2 * k + 1]
    for i in range(q):
        for k in range(n // 2):
            mulv[i] -= B[2 * k][i] * B[2 * k + 1][i]
    if n % 2 != 0:
        for i in range(m):
            for j in range(q):
                C[i][j] = mulh[i] + mulv[j]
                for k in range(1, n, 2):
                    C[i][j] = (C[i][j] + (A[i][k] + B[k - 1][j])
                               * (A[i][k - 1] + B[k][j]))
                C[i][j] = C[i][j] + A[i][n - 1] * B[n - 1][j]
    else:
        for i in range(m):
            for j in range(q):
                C[i][j] = mulh[i] + mulv[j]
                for k in range(1, n, 2):
                    C[i][j] = (C[i][j] + (A[i][k] + B[k - 1][j])
                               * (A[i][k - 1] + B[k][j]))
    return C


def create_random_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = randint(-100, 100)
    return matrix


results = []
data = []
for i in range(17, 21):
    A = create_random_matrix(i, i)
    B = create_random_matrix(i, i)
    data.append([A, B])
algs = [[standart_mtx_mul, 0], [winograd_mtx_mul, 0], [opt_winograd_mtx_mul, 0]]
for mtxs in data:
    for alg in algs:
        alg[1] = 0
    count = 100
    for i in range(count):
        for alg in algs:
            t_begin = ticks_us()
            alg[0](*mtxs)
            t_end = ticks_us()
            alg[1] += t_end - t_begin
    result = [len(mtxs[0])]
    print(len(mtxs[0]), end=',')
    for alg in algs:
        print(f"{alg[1] / count:.3f}", end=',')
        result.append(alg[1]/(count * 1000))
    results.append(result)
    print()

print(results)