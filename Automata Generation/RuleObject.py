# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:54:00 2019

@author: Administrator
"""
#maps rule in base 2 to "keys"

import math


class RuleObject:
    rule = 1
    steps = 4 
    w = ((steps * 2)-1)   
    minRule = 0
    maxRule = 255   
    ruleGrid = 0
    ruleMap = {}
    
    def __init__(self, rule, steps):
        self.rule = rule
        self.steps = steps
        self.w = ((steps * 2)-1)
        #Generate Grid
        self.ruleGrid = [[0 for x in range(self.w)] for y in range(steps)]
        #populate first instance
        self.ruleGrid[0][(math.floor(self.w/2))] = 1
        
        self.ruleMap = self.ruleMapping()
        self.populateGrid()
    #used for "rule"
    def defineKey(self):
        return str(('{0:08b}'.format(self.rule)))
    
    @staticmethod
    #used for 7-0
    def binaryRule(rule):
        return str(('{0:03b}'.format(rule)))
    
    #maps rule in base 2 to "keys"
    def ruleMapping(self):
        binRule = self.defineKey()
        mapList = {}
        j = 0
        for i in reversed(range(8)):
            mapList[self.binaryRule(i)] =  binRule[j:j+1]
            j +=1
        return mapList

    def populateGrid(self):
        checkCells = ''
        nextLine = ''
        for i in range(self.steps - 1):
            for j in range(self.w): 
                if(j == 0):
                    checkCells = "0" + str(self.ruleGrid[i][j]) + str(self.ruleGrid[i][j+1])
                    #print(checkCells)
                elif(j == (self.w -1)):
                    checkCells = str(self.ruleGrid[i][j-1]) + str(self.ruleGrid[i][j]) + "0"
                    #print(checkCells)                
                else:
                    checkCells = str(self.ruleGrid[i][j-1]) + str(self.ruleGrid[i][j]) + str(self.ruleGrid[i][j+1])
                    #print(checkCells)
                nextLine += str(self.ruleMap[checkCells])
            #populate next line
            for k in range(self.w):
                self.ruleGrid[i+1][k] = int(nextLine[k:k+1])
            nextLine = ""
    
    #prints matrix
    def printGrid(self):
        b = ""
        for i in range(self.steps):
            for j in range(self.w): 
                b += str(self.ruleGrid[i][j])
                b += " "
                if(j == (self.w - 1)):
                    b += "\n"
        return b  
    
   
#test object 
#sample = RuleObject(60,25)
#test print
#print(sample.printGrid())
