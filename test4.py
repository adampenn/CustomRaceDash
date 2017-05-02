#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

root = tk.Tk()

style = ttk.Style()
style.configure("Mine.TButton", foreground="red")
style.configure("TProgressbar", foreground='red')

btn = ttk.Button(text="Test")
btn.pack()
ttk.Progressbar(orient="horizontal", length=600, mode="determinate", maximum=4, value=1, style="TProgressbar").pack()
ttk.Progressbar(orient="horizontal", length=600, mode="determinate", maximum=4, value=1).pack()
btn2 = ttk.Button(text="Test", style="Mine.TButton")
btn2.pack()

root.mainloop()
