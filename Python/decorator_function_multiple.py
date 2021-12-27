#!/usr/bin/env python
# coding: utf-8

def repeat(n):
    def dec(genuine_function):
        def new_function(func):
            value = func
            i = 0
            while i < n:
                i += 1
                value = genuine_function(value)
            return value
        return new_function
    return dec


@repeat(2)
def plus_1(x):
    return x + 1


@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3))  # должно выдать 5
print(mul_2(4))  # должно выдать 4
