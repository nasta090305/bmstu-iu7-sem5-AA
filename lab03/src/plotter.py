from matplotlib import pyplot as plt
import pandas as pd
ITERATIONS = 500
fig = plt.figure(figsize=(12,8))
df = pd.read_csv("D:/5sem/aa/lab4/out/out.csv")
x = list(df['threads_cnt'])
y = []
for idx, row in df.iterrows():
    y += [ITERATIONS / (row['avg_t'] / 1000)]
print(x)
print(y)
plt.plot(x, y)
plt.xlabel("Количество используемых потоков")
plt.ylabel("Страниц/с")
plt.title("График зависимости количества страниц обрабатываемых в секунду\nот количества дополнительных потоков\n для устройства с 8 логическими потоками")
plt.savefig('res.png')
plt.show()
