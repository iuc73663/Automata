# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 07:33:14 2018

@author: Administrator
"""

import turtle 

point = turtle.Turtle()
point.speed("slowest")
point.color("Black")

def fibGen(n):
    if n <= 1 :
        return n
    else:
        return fibGen(n-1) + fibGen(n-2)

def fibHelper(n):
    aList = []
    for i in range(n):
        aList.append(fibGen(i))
    return aList     


def square(n):
    for i in range(4):
        point.forward(n)
        point.right(90)

fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34]
factor = 5

for k in range(4):
    #point.forward()
    if k == 0:
        print()
    for i in range(len(fibs)):
        point.down()
        square(fibs[i] * factor)
        point.forward(fibs[i] * factor)
        point.right(90)
        point.forward(fibs[i] * factor)  
        point.up()
    