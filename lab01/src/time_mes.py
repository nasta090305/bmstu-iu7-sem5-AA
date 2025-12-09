from time import process_time_ns, perf_counter_ns
from funcs import *
from faker import Faker
import csv


def write_to_csv(filename, data, headers):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


fake = Faker()

results = []

data = []
for i in range(1, 11):
    data.append([''.join(fake.random_letters(i)), ''.join(fake.random_letters(i))])
algs = [[t_matrix_levenstein, 0], [t_recurs_levenstein, 0], [t_memo_levenstein, 0], [t_damerau_levenstein, 0]]
for words in data:
    for alg in algs:
        alg[1] = 0
    count = 300
    for i in range(count):
        for alg in algs:
            t_begin = perf_counter_ns()
            alg[0](*words)
            t_end = perf_counter_ns()
            alg[1] += t_end - t_begin
    result = []
    print("len:", len(words[0]))
    for alg in algs:
        print(str(alg[0]), alg[1] / count)
        result.append(alg[1]/(count * 1000))
    results.append(result)

data = []
for i in range(11, 101):
    data.append([''.join(fake.random_letters(i)), ''.join(fake.random_letters(i))])
algs = [[t_matrix_levenstein, 0], [t_memo_levenstein, 0], [t_damerau_levenstein, 0]]
for words in data:
    for alg in algs:
        alg[1] = 0
    count = 300
    for i in range(count):
        for alg in algs:
            t_begin = perf_counter_ns()
            alg[0](*words)
            t_end = perf_counter_ns()
            alg[1] += t_end - t_begin
    result = []
    print("len:", len(words[0]))
    for alg in algs:
        print(str(alg[0]), alg[1] / (count * 1000))
        result.append(alg[1]/ (count * 1000))
    result.insert(1, '')
    results.append(result)


write_to_csv("time_mes.csv", results, ["matrix_levenshtein", "recurs_levenshtein",
                                       "memo_levenshtein", "damerau_levenshtein"])