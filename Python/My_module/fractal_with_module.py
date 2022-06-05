import turtle
import sierpinski_function

size = 800
min_L = 10
const = 3 ** 0.5 / 2

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)
Sierpinski(size, -size / 2, -size * const / 2)
turtle.done()
