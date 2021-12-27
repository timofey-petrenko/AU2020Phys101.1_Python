#!/usr/bin/env python3
# coding: utf-8

import numpy as np
from matplotlib import pyplot as pp


MODEL_G = 9.81
MODEL_DT = 0.001

class Body:
    def __init__(self, x, y, vx, vy):
        """
        Создать тело.

        Параметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        """

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.trajectory_x = []
        self.trajectory_y = []

    def change_coords(self, new_x, new_y):
        ''' Задаем новые координаты тела '''
        self.x = float(new_x)
        self.y = float(new_y)
        print(f'Новые координаты =({new_x}, {new_y})')

    def change_velocity(self, new_vx, new_vy):
        ''' Задаем телу новую скорость '''
        self.vx = float(new_vx)
        self.vy = float(new_vy)
        print(f'Новые компоненты скорости =({new_vx}, {new_vy})')

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно\
 записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)

        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT



class Rocket(Body):
    def __init__(self, x, y):
        """
        Создать ракету.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        """
        super().__init__(x, y, 10, 10) # Вызовем конструктор предка — тела,
                                       # т.к. он для ракеты актуален
        self.fuel_speed = 75
        self.mass_change = -2
        self.rocket_mass = 1_000
        self.fuel_mass = 950

    def change_fuel_speed(self, new_fuel_speed):
        ''' Изменим скорость истекания топлива относительно ракеты '''
        self.fuel_speed = float(new_fuel_speed)
        print(f'Теперь топливо истекает со скоростью в {new_fuel_speed} единиц')

    def change_mass_change(self, new_mass_change):
        ''' Изменим скорость изменения массы ракеты '''
        self.mass_change = - abs(float(new_mass_change))
        print(f'Масса ракеты теперь убывает со скоростью в\
 {abs(float(new_mass_change))} единиц')

    def change_rocket_mass(self, new_rocket_mass):
        ''' Изменим массу ракеты '''
        if float(new_rocket_mass) < 0:
            print('Вы что, математик? Отрицательная масса... Фи')
        elif float(new_rocket_mass) >= 0:
            self.rocket_mass = float(new_rocket_mass)
            print(f'Теперь масса ракеты составляет {new_rocket_mass} единиц')

    def change_fuel_percentage(self, new_fuel_percentage):
        ''' Изменим долю топлива в ракете '''
        if 0 <= new_fuel_percentage < 1:
            self.fuel_mass = self.rocket_mass * float(new_fuel_percentage)
            print(f'Теперь топливо составляет аж {new_fuel_percentage} от массы\
 ракеты!')
        else:
            print('Доля в массе не может быть больше единицы\
 или отрицательной!!!')

    def mass_decrement(self):
        ''' Уменьшается масса ракеты '''
        self.fuel_mass = self.fuel_mass + self.mass_change * MODEL_DT
        self.rocket_mass = self.rocket_mass + self.mass_change * MODEL_DT

    def advance(self):
        ''' Опишем движение ракеты '''
        #будем считать, что сопло всегда направлено вниз
        if self.fuel_mass > 0:

            self.trajectory_x.append(self.x)
            self.trajectory_y.append(self.y)
            self.x += self.vx * MODEL_DT
            self.y += self.vy * MODEL_DT
            self.vy -= ((self.fuel_speed * self.mass_change) /\
self.rocket_mass + MODEL_G) * MODEL_DT
            self.mass_decrement()

        else:
            super().advance() # вызовем метод предка — тела, т.к.
                              # и он для ракеты актуален.


b = Body(0, 0, 9, 9)
r = Rocket(0, 0)

bodies = [b, r]
# Дальше мы уже не будем думать, кто тут ёжик, кто ракета, а кто котлета —
# благодаря возможностям ООП будем просто работать со списком тел

# self.fuel_speed = 75
# self.mass_change =  -2
# self.rocket_mass = 1_000
# self.fuel_mass = 950

b.change_velocity(10, 30)
r.change_velocity(10, 30)
r.change_rocket_mass(1)
r.change_fuel_percentage(0.93)
r.change_fuel_speed(50)
r.change_mass_change(-20)


for t in np.arange(0, 2, MODEL_DT): # для всех временных отрезков
    for b in bodies: # для всех тел
        b.advance() # выполним шаг


for b in bodies: # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y) # нарисуем их траектории

pp.show()
