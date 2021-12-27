#!/usr/bin/env python
# coding: utf-8

def egcd(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if num1 == 0 and num2 != 0:
        x = 0
        y = 1
        return x, y, num2
    if num2 == 0 and num1 != 0:
        x = 1
        y = 0
        return x, y, num1
    if num1 == 0 and num2 == 0:
        raise ValueError('Хотя бы одно из чисел должно быть ненулевым!!!')
    else:
        d = egcd(num2 % num1, num1)
        gcd = d[2]
        x = d[1] - (num2 // num1) * d[0]
        y = d[0]
        return x, y, gcd


number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')
result = egcd(number_1, number_2)
print(f'{result[0]}*{number_1} + {result[1]}*{number_2} = {result[2]}')
