# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:32:46 2019

@author: Administrator
"""

import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas 

class TurtleCanvas:
    window = tk.Tk()
    canvas = ScrolledCanvas(master=window, width=800, height=600)
    canvas.pack(fill=tk.BOTH, expand=tk.YES)
    screen = TurtleScreen(canvas)
    turtle = RawTurtle(screen)
    def __init__(self,  x, y):
        cWidth = 800
        cHeight = 600
        self.x = x
        self.y = y
        self.turtle.speed("fastest")
        self.window.geometry('%dx%d+%d+%d' % (cWidth, cHeight, x, y))
        self.canvas.bind('<MouseWheel>', self.zoom)
    def zoom(self,event):
        amount = 0.9 if event.delta < 0 else 1.1
        self.canvas.scale(tk.ALL, 0, 0, amount, amount)
        
    def square(self,sidelength = 50):
        for i in range(4):
            self.turtle.forward(sidelength)
            self.turtle.right(90)
    def triangle(self,sidelength = 50):
        point = self.turtle 
        point.color("black") 
        point.speed("fastest")
        for i in range(3):
            point.forward(sidelength)
            point.right(120)        
        self.window.mainloop()
        
    def star(self,sidelength = 50):
        point = self.turtle 
        point.color("black") 
        point.speed("fastest")
        for i in range(5):
            point.forward(sidelength)
            point.right(145)  
        self.window.mainloop()

    def squareDriver(self,steps):
        i = 0
        for j in range(steps):
            self.square(20 + i)
            self.turtle.right(2)
            i += 1 
            
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
        if not(self.shapeSelect.get() == "") and not(self.step_entry.get() == ""):
            sample = TurtleCanvas(100,250)
            sample.squareDriver(int(self.step_entry.get()))     
            #sample.window.mainloop()             
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Fractal Maker')
        self.grid(column=0, row=0, sticky='nsew')
        
        # get screen width and height
        #screen_width = root.winfo_screenwidth()
        #screen_height = root.winfo_screenheight()
        rootWidth = 250
        rootHeight = 150
        x = 0
        y = 0
        root.geometry('%dx%d+%d+%d' % (rootWidth, rootHeight, x, y))        
        self.root.geometry()

        ttk.Label(self, text='Shape').grid(column=0, row=2, sticky='w')
        self.shapeSelect = ttk.Combobox(self, values=["square", "triangle", "star"])
        self.shapeSelect.grid(column=1, row = 2)
        
        ttk.Label(self, text='Depth').grid(column=0, row=3, sticky='w')
        self.step_entry = ttk.Entry(self, width=6)
        self.step_entry.grid(column=1, row = 3)
        
        self.calc_button = ttk.Button(self, text='Calculate', command=self.calculate)
        self.calc_button.grid(column=0, row=4, columnspan=4)
        

        ttk.Separator(self, orient='horizontal').grid(column=0, row=1, columnspan=4, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)


            
if __name__ == '__main__':
    root = tk.Tk()
    Adder(root)
    root.mainloop()

#sample = TurtleCanvas(200,300)
#sample.squareDriver(30)
#sample.window.mainloop()