# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)


from turtle import *
shape("turtle")

speed("fastest")

i = 0
for j in range(360):
    right(2)
    square(20 + i)
    i += 1 


done()

