import tkinter as tk
from tkinter import ttk
import threading
from threading import Thread
from queue import Queue

app = tk.Tk()
app.button = ttk.Button(text="start")
app.button.pack()
app.RPM = ttk.Progressbar(app, orient="horizontal", length=200, mode="determinate", value=0, maximum=7000)
app.RPM.pack()
app.scale = ttk.Scale(app, from_=0, to=7000, orient="horizontal")
app.scale.pack()


def start(app):
  app.RPM["value"] = 0
  app.RPM["maximum"] = 7000
  get_RPM(app)

def get_RPM(app):
  app.RPM["value"] = app.scale.get()


app.mainloop()

