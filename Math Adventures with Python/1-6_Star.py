# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:17:12 2019

@author: Administrator
"""

from turtle import *

shape("turtle")

speed("fastest")

def star(sidelength):
    for i in range(5):
        forward(sidelength)
        right(145)
     

def starSpiral():
    n = 0
    for k in range(1,60):        
        star(50 + n)
        right(2)
        n += 10
        


starSpiral()

done()