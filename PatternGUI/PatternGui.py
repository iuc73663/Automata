# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:32:46 2019

@author: Administrator
"""

import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas
from win32api import GetSystemMetrics

colors = ["Black", "Red", "Purple", "Blue", "Green", "Yellow", "Orange"]

class TurtleCanvas():


    def __init__(self,master, x, y):
        self.window = master
        self.canvas = ScrolledCanvas(master=self.window, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.screen = TurtleScreen(self.canvas)
        self.turtle = RawTurtle(self.screen)
        cWidth = 600
        cHeight = 600
        self.x = x
        self.y = y
        self.turtle.speed("fastest")
        self.window.geometry('%dx%d+%d+%d' % (cWidth, cHeight, x, y))
        self.canvas.bind('<MouseWheel>', self.zoom)
        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)
        self.canvas.bind("<ButtonPress-3>", self.changeDirection)
        self.window.bind("<c>", self.changeColor)
        self.rightDirection = True
    def changeDirection(self,event):
        #print(self.rightDirection)
        if(self.rightDirection):
            self.rightDirection = False
        else:
            self.rightDirection = True
    def changeColor(self,event):
        currentColorIndex = colors.index(self.turtle.color()[0])
        if (currentColorIndex == (len(colors) - 1)):
            self.turtle.color(colors[0])
        else:
            self.turtle.color(colors[currentColorIndex + 1])
    def scroll_start(self,event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self,event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
    def zoom(self,event):
        amount = 0.9 if event.delta < 0 else 1.1
        self.canvas.scale(tk.ALL, 0, 0, amount, amount)

    def square(self,sidelength = 50):
        for i in range(4):
            self.turtle.forward(sidelength)
            self.turtle.right(90)
    def triangle(self,sidelength = 50):
        for i in range(3):
            self.turtle.forward(sidelength)
            self.turtle.right(120)

    def star(self,sidelength = 50):
        for i in range(5):
            self.turtle.forward(sidelength)
            self.turtle.right(144)

    def shapeDriver(self, shapeFunc, steps):
        self.turtle.st()
        i = 0
        for j in range(steps):
            shapeFunc(1 + i)
            if(self.rightDirection == True):
                self.turtle.right(1)
            else:
                self.turtle.left(1)
            i += 0.1
        self.turtle.ht()
    def helperDriver(self, shape, steps):
        self.window.title(shape + " || Steps:" + str(steps))
        if(shape == "Square"):
            self.shapeDriver(self.square,steps)
        if(shape == "Triangle"):
            self.shapeDriver(self.triangle,steps)
        if(shape == "Star"):
            self.shapeDriver(self.star,steps)
class Adder(ttk.Frame):
    """The adders gui and functions."""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
    def on_quit(self):
        """Exits program."""
        quit()

    def calculate(self):
        if not(self.step_entry.get() == ""):
            self.newWindow = tk.Toplevel(self.master)
            self.canvasObject = TurtleCanvas(self.newWindow,100,250)            
            #reference this amazing thread https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application            
            self.canvasObject.turtle.color(self.colorSelect.get())
            self.canvasObject.helperDriver(self.shapeSelect.get(),int(self.step_entry.get()))
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Goat Simulator')
        self.grid(column=0, row=0, sticky='nsew')
        rootWidth = GetSystemMetrics(0)
        rootHeight = GetSystemMetrics(1)
        x = 0
        y = 0
        root.geometry('%dx%d+%d+%d' % (rootWidth, rootHeight, x, y))
        self.root.geometry()

        ttk.Label(self, text='Shape').grid(column=0, row=2, sticky='w')
        self.shapeSelect = ttk.Combobox(self, values=["Square", "Triangle", "Star"])
        self.shapeSelect.current(0)
        self.shapeSelect.grid(column=1, row = 2)

        ttk.Label(self, text='Color').grid(column=0, row=3, sticky='w')
        self.colorSelect = ttk.Combobox(self, values = colors)
        self.colorSelect.current(0)
        self.colorSelect.grid(column=1, row = 3)

        ttk.Label(self, text='Depth').grid(column=0, row=4, sticky='w')
        self.step_entry = ttk.Entry(self, width=6)
        self.step_entry.insert(0,"30")
        self.step_entry.grid(column=1, row = 4)

        self.calc_button = ttk.Button(self, text='Calculate', command=self.calculate)
        self.calc_button.grid(column=0, row=5, columnspan=4)
        
        self.testCanvas = ScrolledCanvas(master=self.root, width=800, height=600)
        self.screen = TurtleScreen(self.testCanvas)
        self.turtle = RawTurtle(self.screen)
        self.testCanvas.grid(column=0,row=8,columnspan = 8)
        
        
        ttk.Separator(self, orient='horizontal').grid(column=0, row=1, columnspan=4, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)



if __name__ == '__main__':
    root = tk.Tk()
    #root.attributes("-fullscreen", True) #literal fullscreen
    Adder(root)
    root.mainloop()

#sample = TurtleCanvas(200,300)
#sample.squareDriver(30)
#sample.window.mainloop()
