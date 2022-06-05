#!/usr/bin/env python3
# coding: utf-8


import csv
import numpy as np
import pandas
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats


values = []
with open('coin_flip.csv', mode='r') as file:
    csvFile = csv.reader(file)
    next(csvFile)
    for line in csvFile:
        values.append(line[1])
values = [int(val) for val in values]
values = np.array(values)

set_of_vals = []
k = 0
while k < 10:
  set_of_vals.append(sum(values[10 * k : 10 * (k + 1)]))
  k += 1

plt.plot(list(range(len(set_of_vals))), set_of_vals)
plt.title('Результат бросания монетки (0 - решка, 1 - орел, по десять бросков за раз)')
plt.ylabel('Результат десяти бросков')
plt.xlabel('Номер опыта')
plt.show()

df = pandas.DataFrame(data={
    'coin_flips_total': set_of_vals
})

df.to_csv("coin_flips_total.csv")

df1 = pandas.read_csv("coin_flips_total.csv")

df2 = df1["coin_flips_total"]
df2.plot(kind='bar')
plt.title('Результат бросания монетки (0 - решка, 1 - орел, по десять бросков за раз)')
plt.ylabel('Результат десяти бросков')
plt.xlabel('Номер опыта')

print(df2.describe())

my_data = pandas.DataFrame(data={
    "value": df2
})

print(stats.kstest(my_data["value"], "norm", (my_data["value"].mean(), my_data["value"].std()), 
          N=len(my_data["value"])))
