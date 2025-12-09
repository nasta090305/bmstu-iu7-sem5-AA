from matplotlib import pyplot as plt
import csv

with open("time_mes.csv") as f:
    data = list(csv.reader(f))
    algs, data = data[0], data[1:]

matrix_levenstein = [float(data[i][0]) for i in range(len(data))]
recurs_levenstein = [float(data[i][1]) if data[i][1] != '' else None for i in range(len(data))]
memo_levenstein = [float(data[i][2]) for i in range(len(data))]
damerau_levenstein = [float(data[i][3]) for i in range(len(data))]

plt.plot(matrix_levenstein, 'r-', label='matrix_levenshtein')
#plt.plot(recurs_levenstein, 'b--', label='recurs_levenshtein')
plt.plot(memo_levenstein, "y-.", label='memo_levenshtein')
plt.plot(damerau_levenstein, "g:", label='damerau_levenshtein')
plt.legend()
plt.xlabel("Длина слов")
plt.ylabel("Время работы алгоритма в мкс")
plt.show()