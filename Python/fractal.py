#!/usr/bin/env python
# coding: utf-8

import turtle


size = 800
min_L = 10
const = 3 ** 0.5 / 2
 
def Sierpinski(L, x, y):
    if L > min_L:
        L = L / 2
        Sierpinski(L, x, y)
        Sierpinski(L, x + L, y)
        Sierpinski(L, x + L / 2, y + L * const)
    else:
        t.goto(x ,y)
        t.pendown()
        t.begin_fill()
        t.forward(L)
        t.left(120)
        t.forward(L)
        t.left(120)
        t.forward(L)
        t.end_fill()
        t.setheading(0)
        t.penup()
        t.goto(x, y)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)
Sierpinski(size, -size / 2, -size * const / 2)
turtle.done()
