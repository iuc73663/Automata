# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:10:45 2019

@author: Administrator
"""

def a(x):
    return "a(%s)" % (x,)

def b(f,x):
    return f(x)

print(b(a,10))