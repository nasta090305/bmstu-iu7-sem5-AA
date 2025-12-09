from utime import ticks_ms
import random as rd
def matrix_mull(a : list[list[int]], b : list[list[int]]) -> list[list[int]]:
    n1, m1 = len(a), len(a[0])
    n2, m2 = len(b), len(b[0])
    res : list[list[int]] = [[0 for _ in range(m2)] for _ in range(n1)]
    
    for i in range(n1):
        for j in range(m2):
            for k in range(n2):
                res[i][j] += a[i][k] * b[k][j] #res[i][j] += -> res[i][j] = res[i][j] + -> 6
                                               # a[i] += -> a[i] = a[i] +
    return res
    
def Winograd_matrix_mull(a : list[list[int]], b : list[list[int]]) -> list[list[int]]:
    
    n1, m1 = len(a), len(a[0]) #2 + 2nn
    m2 = len(b[0])

    res : list[list[int]] = [[0 for _ in range(m2)] for _ in range(n1)]

    a_tmp = [0] * n1
    for i in range(n1):
        for j in range(0, m1 // 2, 1):
            a_tmp[i] = a_tmp[i] + a[i][2 * j] * a[i][2 * j + 1]

    b_tmp = [0] * m2
    for i in range(m2):
        for j in range(0, m1 // 2, 1):
            b_tmp[i] = b_tmp[i] + b[2 * j][i] * b[2 * j + 1][i]

    for i in range(n1):
        for j in range(m2):
            res[i][j] = -a_tmp[i] - b_tmp[j]

            for u in range(0, m1 // 2, 1):
                res[i][j] = res[i][j] + (a[i][2 * u + 1] + b[2 * u][j]) * \
                                  (a[i][2 * u] + b[2 * u + 1][j])

    if m1 % 2 == 1:
        for i in range(n1):
            for j in range(m2):
                res[i][j] = res[i][j] + a[i][m1 - 1] * b[m1 - 1][j]

    return res

def Winograd_matrix_mull_optimized(a : list[list[int]], b : list[list[int]]) -> list[list[int]]:
    n1, m1 = len(a), len(a[0])
    m2 = len(b[0])

    res : list[list[int]] = [[0 for _ in range(m2)] for _ in range(n1)]

    a_tmp = [0] * n1

    for j in range(0, m1 // 2, 1):
        a_tmp[0] = a_tmp[0] - a[0][j<<1] * a[0][(j<<1) + 1]

    for i in range(1, n1):
        for j in range(0, m1 // 2, 1):
            a_tmp[i] = a_tmp[i] - a[i][j<<1] * a[i][(j<<1) + 1]

    b_tmp = [0] * m2

    for j in range(0, m1 // 2, 1):
        b_tmp[0] = b_tmp[0] - b[j<<1][0] * b[(j<<1) + 1][0]
    
    for i in range(1, m2):
        for j in range(0, m1 // 2, 1):
            b_tmp[i] = b_tmp[i] - b[j<<1][i] * b[(j<<1) + 1][i]

    for j in range(m2):
        res[0][j] = a_tmp[0] + b_tmp[j]

        for u in range(0, m1 // 2, 1):
            res[0][j] = res[0][j] + (a[0][(u<<1) + 1] + b[u<<1    ][j]) * \
                                (a[0][u<<1    ] + b[(u<<1) + 1][j])

    for i in range(1, n1):
        for j in range(m2):
            res[i][j] = a_tmp[i] + b_tmp[j]

            for u in range(0, m1 // 2, 1):
                res[i][j] = res[i][j] + (a[i][(u<<1) + 1] + b[u<<1    ][j]) * \
                                  (a[i][u<<1    ] + b[(u<<1) + 1][j])

    if m1 % 2 == 1:

        for j in range(m2):
            res[0][j] = res[0][j] + a[0][m1 - 1] * b[m1 - 1][j]

        for i in range(1, n1):
            for j in range(m2):
                res[i][j] = res[i][j] + a[i][m1 - 1] * b[m1 - 1][j]

    return res


def get_rand_mtx(size : int) -> list[list[int]]:
    return [[rd.randint(-100, 100) for _ in range(size)] for _ in range(size)]

def get_alg_time(func, data_1, data_2) -> float:
   begin_time = ticks_ms()
   func(data_1, data_2)
   return (ticks_ms() - begin_time)

def avg_execution_time(excecution_range : list[int], function, data_gen, iterations : int) -> list[float]:
   data : list[float] = []
   for i in excecution_range:
       s = 0.0
       for _ in range(iterations):
           m1, m2 = data_gen(i), data_gen(i)
           s += get_alg_time(function, m1, m2)
       data += [s]
       print(f'Executed all {function.__name__} instances for {i} out of {excecution_range[-1]}.')
   return data
 
def bench():
   ITER = 200
   algos = [matrix_mull, Winograd_matrix_mull, Winograd_matrix_mull_optimized]
   LENS_REC : list[int]= list(range(1, 15))
   d = {'LENS' : LENS_REC}
   for alg in algos:
        data : list[float] = []
        data = avg_execution_time(LENS_REC, alg, get_rand_mtx, ITER)
        d[alg.__name__] = data
   print(d)
 
if __name__ == '__main__':
   bench()