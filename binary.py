# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:11:07 2019

@author: Administrator
"""

def defineKey(rule):
    return ('{0:08b}'.format(rule))

def binaryRule(rule):
    return ('{0:08b}'.format(rule))

b = binaryRule(30)

print(b)