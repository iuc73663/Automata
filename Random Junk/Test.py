# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:17:38 2018

@author: Kevin
"""
import tkinter as tk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas 

def zoom(event):
    amount = 0.9 if event.delta < 0 else 1.1

    canvas.scale(tk.ALL, 0, 0, amount, amount)


def triangle(point, length):
    for i in range(4):
        point.forward(length)
        point.right(90)
        point.ht()
  

def driver():
    point = turtle
    point.speed("fastest")
    point.color("blue")
    tilt = 1
    for i in range(1,5):
        point.right(5)
        triangle(point, 1 + tilt)
        tilt += 1
    
class Adder(tk.Frame):
    """The adders gui and functions."""
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        """Exits program."""
        quit()

    def init_gui(self): 
        """Builds GUI."""
        self.root.title('Fractals')
        self.grid(column=0, row=0, sticky='nsew')



        self.answer_frame = tk.LabelFrame(self, text='Output',
                height=100)
        self.answer_frame.grid(column=0, row=4, columnspan=4, sticky='nesw')

        self.answer_label = tk.Label(self.answer_frame, text='')
        self.answer_label.grid(column=0, row=0)


        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)


if __name__ == '__main__':
    root = tk.Tk()
    Adder(root)
    root.mainloop()









