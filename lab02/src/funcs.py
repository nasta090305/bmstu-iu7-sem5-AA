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
                C[i][j] = C[i][j] + A[i][n - 1] * B[n -8  1][j]
    else:
        for i in range(m):
            for j in range(q):
                C[i][j] = mulh[i] + mulv[j]
                for k in range(1, n, 2):
                    C[i][j] = (C[i][j] + (A[i][k] + B[k - 1][j])
                               * (A[i][k - 1] + B[k][j]))
    return C


def scan_matrix():
    try:
        n = int(input("Введите количество строк: "))
        m = int(input("Введите количество столбцов: "))
        if n < 1 or m < 1:
            return None
    except:
        return None
    try:
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(int(input("Введите элемент матрицы: ")))
        print()
        return matrix
    except:
        print()
        return None

def print_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(" " + str(matrix[i][j]), end = "")
        print("")