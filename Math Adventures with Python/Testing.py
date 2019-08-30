# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:32:46 2019

@author: Administrator
"""

import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas 

def square(point,sidelength = 50):
    for i in range(4):
        point.forward(sidelength)
        point.right(90)
def triangle(point,sidelength = 50):
    for i in range(3):
        point.forward(sidelength)
        point.right(120)        

def star(point, sidelength = 50):
    for i in range(5):
        point.forward(sidelength)
        point.right(145)  
def driver(shape, turt):
    point = turt 
    point.color("black") 
    point.speed("fastest")
    if(shape == "triangle"):
        i = 0
        for j in range(60):
            point.right(2)
            triangle(point, 20 + i)
            i += 1 
    if(shape == "square"):
        i = 0
        for j in range(60):
            point.right(2)
            square(point, 20 + i)
            i += 1 
    if(shape == "star"):
        i = 0
        for j in range(60):
            point.right(2)
            star(point, 20 + i)
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
        if not(self.shapeSelect.get() == ""):
            window = tk.Tk()
            canvas = ScrolledCanvas(master=window, width=800, height=600)
            canvas.pack(fill=tk.BOTH, expand=tk.YES)
            screen = TurtleScreen(canvas)
            turtle = RawTurtle(screen)
            cWidth = 800
            cHeight = 600
            x = 300
            y = 100
            window.geometry('%dx%d+%d+%d' % (cWidth, cHeight, x, y))
            driver(self.shapeSelect.get(), turtle)                    
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
        
        self.calc_button = ttk.Button(self, text='Calculate', command=self.calculate)
        self.calc_button.grid(column=0, row=3, columnspan=4)
        

        ttk.Separator(self, orient='horizontal').grid(column=0, row=1, columnspan=4, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)



if __name__ == '__main__':
    root = tk.Tk()
    Adder(root)
    root.mainloop()
