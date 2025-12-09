from time import process_time_ns, perf_counter_ns
from funcs import *
import csv
from random import randint


def create_random_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = randint(-100, 100)
    return matrix


def write_to_csv(filename, data, headers):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

results = []

data = []
for i in range(100, 1001, 100):
    A = create_random_matrix(i, i)
    B = create_random_matrix(i, i)
    data.append([A, B])
algs = [[standart_mtx_mul, 0], [winograd_mtx_mul, 0], [opt_winograd_mtx_mul, 0]]
for mtxs in data:
    for alg in algs:
        alg[1] = 0
    count = 10
    for i in range(count):
        for alg in algs:
            t_begin = process_time_ns()
            alg[0](*mtxs)
            t_end = process_time_ns()
            alg[1] += t_end - t_begin
    result = [len(mtxs[0])]
    print("len:", len(mtxs[0]))
    for alg in algs:
        print(str(alg[0]), alg[1] / count)
        result.append(alg[1]/(count * 1000))
    results.append(result)

pretty_data = []
for i in results:
    line = [i[0]]
    for j in i[1:]:
        if j == '':
            line.append('')
        else:
            line.append(f"{float(j):.3f}")
    pretty_data.append(line)
write_to_csv("time_mes.csv", pretty_data, ["size", "standart", "winograd", "opt_winograd"])