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
    right(135)
    forward(a)

def main():
    fillcolor("blue")
    begin_fill()
    triangle_1(100,50,50)
    end_fill()
    fillcolor("orange")
    begin_fill()
    square_1(50, 50, 25*math.sqrt(2))
    end_fill()
    fillcolor("purple")
    begin_fill()
    triangle_5(50,50,25*math.sqrt(2), 50)
    end_fill()
    turtle.done()

main()










