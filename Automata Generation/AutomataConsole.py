"""
AutomataConsole.py
~~~~~~

Creates a simple GUI for summing two numbers.
"""

import tkinter as tk
from tkinter import ttk
import RuleObject as automata



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
        
        rule = int(self.rule_entry.get())
        steps = int(self.step_entry.get())
        
        ruleGen = automata.RuleObject(rule,steps)
        self.answer_label['text'] = ruleGen.printGrid()

    def init_gui(self):
        """Builds GUI."""
        self.root.title('Automata')
        self.grid(column=0, row=0, sticky='nsew')



        self.rule_entry = ttk.Entry(self, width=5)
        self.rule_entry.grid(column=1, row = 2)
        
        self.step_entry = ttk.Entry(self, width=5)
        self.step_entry.grid(column=3, row = 2)


        self.calc_button = ttk.Button(self, text='Calculate', command=self.calculate)
        self.calc_button.grid(column=0, row=3, columnspan=4)

        self.answer_frame = ttk.LabelFrame(self, text='Output',
                height=100)
        self.answer_frame.grid(column=0, row=4, columnspan=4, sticky='nesw')

        self.answer_label = ttk.Label(self.answer_frame, text='')
        self.answer_label.grid(column=0, row=0)

        # Labels that remain constant throughout execution.
        ttk.Label(self, text='Rule').grid(column=0, row=2, sticky='w')
        
        ttk.Label(self, text='Steps').grid(column=2, row=2,
                sticky='w')

        ttk.Separator(self, orient='horizontal').grid(column=0,
                row=1, columnspan=4, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    Adder(root)
    root.mainloop()