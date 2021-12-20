#!/usr/bin/env python
# coding: utf-8

import numbers


N = int(input('Определитесь по какому положительному модулю будем\
 рассматривать числа'))

class ModularInteger():
    '''Класс чисел по модулю'''

    def __init__(self, arg):
        if isinstance(arg, numbers.Integral):
            self.value = arg % N
        else:
            raise TypeError('Простите, принимаем только целые числа!!!')

    def __str__(self):
        return str(self.value) + ' mod ' + str(N)

    def __eq__(self, other):
        ''' Равенство '''
        if isinstance(other, ModularInteger):
            if (self.value - other.value) % N == 0:
                return True
        else:
            raise TypeError('Хочешь что-то сделать с переменной - \
сделай ее экземляром чисел mod N.')

    def __add__(self, other):
        '''Сложение'''
        if isinstance(other, ModularInteger):
            my_sum = (self.value + other.value) % N
            my_sum = ModularInteger(my_sum)
            return my_sum
        else:
            raise TypeError('Ты правда думаешь, что я могу сложить ТАКОЕ? \
Хочешь что-то сделать с переменной - сделай ее экземляром чисел mod N. ')

    def __mul__(self, other):
        '''Умножение'''
        if isinstance(other, ModularInteger):
            my_product = (self.value * other.value) % N
            my_product = ModularInteger(my_product)
            return my_product
        else:
            raise TypeError('Я отказываюсь ЭТО перемножать. \
Хочешь что-то сделать с переменной - сделай ее экземляром чисел mod N.')

    def __radd__(self, other):
        '''Сложение в другом порядке'''
        return self.__add__(other)

    def __rmul__(self, other):
        '''Умножение в другом порядке'''
        return self.__mul__(other)

    def __sub__(self, other):
        '''Вычитание'''
        if isinstance(other, ModularInteger):
            my_diff = (self.value - other.value) % N
            my_diff = ModularInteger(my_diff)
            return my_diff
        else:
            raise TypeError('Ты так хочешь меня сломать? \
Хочешь что-то сделать с переменной - сделай ее экземляром чисел mod N.')

    def __neg__(self):
        '''Противоположный элемент'''
        my_neg = - self.value % N
        my_neg = ModularInteger(my_neg)
        return my_neg

    def __rsub__(self, other):
        '''Вычитание в другом порядке'''
        return self.__neg__().__sub__(other)

two_numbers = input('Введите два числа').split()
two_numbers = [int(el) for el in two_numbers]
x, y = two_numbers[0], two_numbers[1]
x = ModularInteger(x)
y = ModularInteger(y)
print('Первое число равно ', str(x))
print('Число, противоположное первому, равно ', str(-x))
print('Первое плюс второе равно ', str(x + y))
print('Второе плюс первое равно', str(y + x))
print('Первое минус второе равно', str(x - y))
print('Второе минус первое равно', str(y - x))
print('Первое на второе равно', str(x * y))
print('Второе на первое равно', str(y * x))
if x == y:
    print('Числа равны')
else:
    print('Числа не равны')
