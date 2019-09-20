# Case-study #1
# Developers:  Revtova L. (30%)
#              Nikitina A. (30%)
#              Arhipova A (30%)

import turtle
from turtle import *
import math

def triangle_1(x, y, a):
    up()
    setposition(x, y)
    forward(a)
    down()
    right(90)
    forward(a)
    right(90)
    forward(a)
    right(135)
    forward(a*(math.sqrt(2)))

def square_1(x,y,a):
    up()
    setposition(x, y)
    down()
    right(360)
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)

def triangle_5(x,y,a,b):
    up()
    setposition(x,y)
    down()
    right(90)
    forward(2*a)
    right(135)
    forward(b)
    right(45)
    forward(a)

def main():
    triangle_1(50,50,50)
    square_1(50, 50, 25*math.sqrt(2))
    triangle_5(50,50,25*math.sqrt(2), 50)
    turtle.done()

main()









