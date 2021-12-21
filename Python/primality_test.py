#!/usr/bin/env python
# coding: utf-8

import math


def is_prime(num):
    """Говорит, верно ли, что число простое"""
    try:
        num = int(num)
        if num <= 1:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        k = 2
        while i < math.ceil(num ** 0.5):
            if num % i == 0:
                return False
            i += k
            k = 6 - k
        return True
    except ValueError:
        print('Просили ли же: ЦЕЛОЕ ЧИСЛО!')

number = input('Введите целое число')
print(is_prime(number))