# -*- coding: utf-8 -*-
"""
Spyder Editor

Make a function to draw 60 squares, turning 5 degrees after each square and
making each successive square bigger. Start at a length of 5 and increment
5 units every square.
"""
from turtle import *

def square(sidelength = 5):
    for i in range(4):
        forward(sidelength)
        right(90)
        

shape("turtle")

speed("normal")




        
n = 0
for k in range(1,60):        
    square(5 + n)
    right(5)
    n += 1

done()