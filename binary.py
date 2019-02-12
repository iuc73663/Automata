# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:11:07 2019

@author: Administrator
"""

import math

#used for "rule"
def defineKey(rule):
    return ('{0:08b}'.format(rule))

#used for 7-0
def binaryRule(rule):
    return ('{0:03b}'.format(rule))

#maps rule in base 2 to "keys"
def ruleMapping(rule):
    binRule = defineKey(rule)
    mapList = {}
    j = 0
    for i in reversed(range(8)):
        mapList[binaryRule(i)] =  binRule[j:j+1]
        j +=1
    return mapList

#prints matrix
def printGrid(grid, r,c):
    b = ""
    for i in range(r):
        for j in range(c): 
            b += str(grid[i][j])
            b += " "
            if(j == (c - 1)):
                b += "\n"
    print(b)

#hard coded rule---------
rule = 60
ruleMap = ruleMapping(rule)
#------------------------
#hard coded steps (rows) 
h = 30
#columns
w = ((h * 2)-1)
#create grid based on above
ruleGrid = [[0 for x in range(w)] for y in range(h)]
#step 1
ruleGrid[0][(math.floor(w/2))] = 1


#populate matrix
def populateGrid(grid, r,c):
    checkCells = ''
    nextLine = ''
    for i in range(r - 1):
        for j in range(c): 
            if(j == 0):
                checkCells = "0" + str(grid[i][j]) + str(grid[i][j+1])
                #print(checkCells)
            elif(j == (c-1)):
                checkCells = str(grid[i][j-1]) + str(grid[i][j]) + "0"
                #print(checkCells)                
            else:
                checkCells = str(grid[i][j-1]) + str(grid[i][j]) + str(grid[i][j+1])
                #print(checkCells)
            nextLine += str(ruleMap[checkCells])
        #populate next line
        for k in range(c):
            grid[i+1][k] = int(nextLine[k:k+1])
        nextLine = ""
    
    #print preview
    printGrid(grid,r,c)

#preview
#populateGrid(ruleGrid,h,w)


