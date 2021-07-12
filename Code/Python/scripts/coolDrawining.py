#!/bin/env python

from turtle import *
color('green')
bgcolor('black')
speed(11)
hideturtle()
b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1


#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()
