#!/usr/bin/env python3
# coding: utf-8


import csv
import numpy as np
import pandas
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats


values = []
with open('coin_flip.csv', mode='r') as file: #открываем исходный файл, в котором есть 100 измерений бросков монетки
    csvFile = csv.reader(file) # читаем файл
    next(csvFile)              # пропускаем строку с названиями
    for line in csvFile:
        values.append(line[1]) # добавляем все значения показаний монетки в один список
values = [int(val) for val in values] # и делаем их целочисленными
values = np.array(values)

set_of_vals = []
k = 0
while k < 10:
  set_of_vals.append(sum(values[10 * k : 10 * (k + 1)]))
  k += 1             #разбиваем на серию из десяти измерений, в каждой из которых мереется сумма 10 бросков монетки

plt.plot(list(range(len(set_of_vals))), set_of_vals) #изображаем график
plt.title('Результат бросания монетки (0 - решка, 1 - орел, по десять бросков за раз)')
plt.ylabel('Результат десяти бросков')
plt.xlabel('Номер опыта')
plt.show()

df = pandas.DataFrame(data={
    'coin_flips_total': set_of_vals
})                                  #используем для анализа данных pandas

df.to_csv("coin_flips_total.csv")  #сохраняем в виде файла, в котором, в отличие от предыдущего, 10 измерений по 10

df1 = pandas.read_csv("coin_flips_total.csv") #считываем этот файл

df2 = df1["coin_flips_total"] #при построении гистограммы нас не интересуют номера экспериментов - только значения
df2.plot(kind='bar')  #строим гистограмму
plt.title('Результат бросания монетки (0 - решка, 1 - орел, по десять бросков за раз)')
plt.ylabel('Результат десяти бросков')
plt.xlabel('Номер опыта')

print(df2.describe()) #описываем статистические показатели

print(stats.kstest(df2, "norm", (df2.mean(), df2.std()), 
          N=len(df2))) #описываем статистические показатели
