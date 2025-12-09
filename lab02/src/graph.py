from matplotlib import pyplot as plt
import csv

with open("time_mes.csv") as f:
    data = list(csv.reader(f))
    algs, data = data[0], data[1:]

sizes = [float(data[i][0]) for i in range(len(data))]
standart = [float(data[i][1]) for i in range(len(data))]
winograd = [float(data[i][2]) for i in range(len(data))]
opt_winograd = [float(data[i][3]) for i in range(len(data))]

plt.plot(sizes, standart, 'r-', label='standart')
plt.plot(sizes, winograd, "y-.", label='winograd')
plt.plot(sizes, opt_winograd, "g:", label='opt_winograd')
plt.legend()
plt.xlabel("Размер матрицы")
plt.ylabel("Время работы алгоритма в мкс")
plt.show()