# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 11:32:56 2018

@author: Administrator
Square Fractals

"""
import turtle 
import math

def getPoints(scale,shift, angle):
    points = [[-20,-10],[-20,30],[20,30],[20,-10]]
    for i in range(len(points)):
        for j in range(len(points[i])):
            points[i][j]*= scale
            points[i][j]+= shift
            #print(points[i][j])
    n = getXY(points,angle)     
    return n

def getMid(p1,p2):
    return (((p1[0] + p2[0])/2),((p1[1]+p2[1])/2))


def square(point,points,depth):

    point.up()
    point.goto(points[0][0],points[0][1])
    point.down()
    point.color("purple")
    point.goto(points[1][0],points[1][1])
    point.color("red")
    point.goto(points[2][0],points[2][1])
    point.color("blue")
    point.goto(points[3][0],points[3][1]) 
    point.color("orange")
    point.goto(points[0][0],points[0][1])

    if depth>0:
        square(point,[getMid(points[0], points[1]),
                        getMid(points[1], points[2]),
                        getMid(points[2], points[3]),
                        getMid(points[3], points[0])],
                   depth-1)
           
         
def getXY(aList, a):
    m = []
    
    for i in range(len(aList)):  
        x =  (math.cos(a) * aList[i][0]) + (aList[i][1] * math.sin(a))   
        y =  ((-1 * math.sin(a) * aList[i][0])+(math.cos(a) * aList[i][1]))   
        m.append([x,y])
    return m


def driver(depth,speed,color,scale,shift,angle):
    point = turtle.Turtle()
    point.speed(speed)
    point.color(color)
    
    square(point,getPoints(scale,shift,angle),depth)
    point.ht()

    


colors = ['orange','red','violet','purple','blue','black']     

shift = 0.0

angle = 2
circle = 360/angle
radians = angle * (3.1415/180)

for i in range(int(circle * 2)):
    driver(4,'fastest',colors[i%len(colors)],6,shift,(radians * i))
    shift += .1

