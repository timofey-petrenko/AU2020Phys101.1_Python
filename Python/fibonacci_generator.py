#!/usr/bin/env python3
# coding: utf-8

class Fib:
    def __init__(self, stop):
        self.value1 = 1
        self.value2 = 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value1 >= self.stop:
            raise StopIteration
        i = self.value1
        j = self.value2
        self.value1 = j
        self.value2 = i + j
        return i

stop_point = int(input('Вплоть до какого числа Вы хотите выводить числа Фибоначчи?'))
f_num = Fib(stop_point)
for f in f_num:
    print(f)
