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