# libs
import tkinter as tk

# scripts
from core import Engine

class CalculatorGUI:
    def __init__(self, engine):
        self.engine = engine

        # gui
        self.root = tk.Tk()
        self.root.title("Premordial calculator")
        self.root.geometry("400x300")

    def run_loop(self):
        self.root.mainloop()
    
