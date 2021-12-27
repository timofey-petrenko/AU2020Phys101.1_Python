#!/usr/bin/env python3
# coding: utf-8

def gcd(a, b):
    a = int(a)
    b = int(b)
    if a == 0 and b != 0:
        return abs(b)
    if b == 0 and a != 0:
        return abs(a)
    if a == 0 and b == 0:
        raise ValueError('Хотя бы одно из чисел должно быть ненулевым!!!')
    else:
        return abs(gcd(b, a % b))

number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')
g = gcd(number_1, number_2)
print(g)
