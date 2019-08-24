# -*- coding: utf-8 -*-
"""
Spyder Editor

A Circle of Squares
Write and run a function that draws 60 squares, turning right 5 degrees after
each square. Use a loop!
"""

from turtle import *
shape('turtle')
def square():
    for i in range(4):
        forward(100)
        right(90)
speed("fastest")
for j in range(0,60):
    right(5)
    square()
    
done()