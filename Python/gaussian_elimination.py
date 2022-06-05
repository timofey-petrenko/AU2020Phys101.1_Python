#!/usr/bin/env python3
# coding: utf-8

#Решим систему уравнений Ax=b, где A - некая матрица, x и b векторы, и у системы существует единственное решение.


import numpy as np
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box
#Импортируем numpy, чтобы работать с массивами и векторами

def gauss(A, b):
    """ Эта функция решает систему линейных уравнений по методу Гаусса 
    (при условии, что у системы есть решение и оно единственное) """
    A_b = np.concatenate((A, b[:, None]), axis=1)
    A_b_length = len(A_b)

    def forward():
        """Прямой ход"""
        for i in range(A_b_length):
            A_b[i] = A_b[i] / A_b[i, i] #делим коэффициенты всех элементов строки на тот, что на диагонали
            for j in range(i + 1, A_b_length):
                A_b[j] -= A_b[i] * A_b[j, i] # вычитаем домноженные элементы строки из последующих строк

    def backward():
        """Обратный ход"""
        for i in range(A_b_length - 1, 0, -1):
            for j in range(A_b_length - 1, -1, -1):
                if (i - 1) < j:
                    A_b[i - 1, A_b_length] -= A_b[j, A_b_length] * A_b[i - 1, j] #подставляем
        return A_b[:, -1]            
    forward()
    x = backward() #возвращаем крайний справа столбец, получившийся после элементарных преобразований - наш ответ.
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

solution = gauss(a, b)
oob_solution = solve_out_of_the_box(a, b)

print(solution)
print("Максимальное отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
