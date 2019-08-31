# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 09:32:03 2018

@author: Administrator
"""

import tkinter as tk
import math
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas 

def zoom(event):
    amount = 0.9 if event.delta < 0 else 1.1
    canvas.scale(tk.ALL, 0, 0, amount, amount)

root = tk.Tk()
canvas = ScrolledCanvas(master=root, width=2000, height=2000)
canvas.pack(fill=tk.BOTH, expand=tk.YES)

screen = TurtleScreen(canvas)
turtle = RawTurtle(screen)


def getPoints(scale,shift, angle):
    points = [[-20,-10],[-20,30],[20,-10]]
    for i in range(len(points)):
        for j in range(len(points[i])):
            points[i][j]*= scale
            points[i][j]+= shift
            #print(points[i][j])
    n = getXY(points,angle)     
    return n

def getMid(p1,p2):
    return (((p1[0] + p2[0])/2),((p1[1]+p2[1])/2))

def triangle(point,points,depth):

    point.up()
    point.goto(points[0][0],points[0][1])
    point.down()
    point.goto(points[1][0],points[1][1])
    point.goto(points[2][0],points[2][1])
    point.goto(points[0][0],points[0][1])

    if depth>0:
        triangle(point,[points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   depth-1)
        triangle(point, [points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   depth-1)
        triangle(point,[points[2],
                         getMid(points[2], points[1]),
                         getMid(points[0], points[2])],
                   depth-1)

def getXY(aList, a):
    m = []
    
    for i in range(len(aList)):  
        x =  (math.cos(a) * aList[i][0]) + (aList[i][1] * math.sin(a))   
        y =  ((-1 * math.sin(a) * aList[i][0])+(math.cos(a) * aList[i][1]))   
        m.append([x,y])
    return m


def driver(depth,speed,color,scale,shift,angle):
    point = turtle
    point.speed(speed)
    point.color(color)
    
    triangle(point,getPoints(scale,shift,angle),depth)
    point.ht()

    


colors = ['orange','red','violet','purple','blue','black']     

shift = 0.0

for i in range(100):
    driver(0,'fastest',colors[i%len(colors)],12,shift,(i/100))
    shift += .1



canvas.bind('<MouseWheel>', zoom)

screen.mainloop()