#!/usr/bin/python3

# System modules
import tkinter as tk
import serial
import socket
import time
from dashSpecs import *
from tkinter import ttk
from queue import Queue
from threading import Thread

def updateGauges(app):
  print("*** Update thread running")
  blink = 0
  while True:
    time.sleep(.05)
    value = app.slider.get()
    app.pb["value"] = value
    if value > RPM_RED_LINE:
      if blink % 2:
        app.style.configure("TProgressbar", background='red', forground='red', thickness=100)
      else:
        app.style.configure("TProgressbar", background='white', forground='white', thickness=100)
      blink = blink + 1
    elif value > RPM_WARNING:
      app.style.configure("TProgressbar", background='yellow', forground='yellow', thickness=100)
    else:
      app.style.configure("TProgressbar", background='white', forground='white', thickness=100)

class main(tk.Tk):
  def __init__(self):
    # Init
    tk.Tk.__init__(self)
    self.style = ttk.Style()
    self.style.configure("TProgressbar", background='red', forground='red', thickness=100)
    self.geometry('800x480')
    #s.theme_use("calm")
    self.pb = ttk.Progressbar(self, orient="vertical", style="TProgressbar", value=50, maximum=RPM_MAX, length=450)
    self.pb.grid(row=1, sticky='W')
    self.slider = ttk.Scale(self, from_=0, to=RPM_MAX, length=400, orient="horizontal")
    self.slider.grid(row=2, column=0)

print('*** Main thread running')

app = main()

update = Thread(target=updateGauges, args=(app,))
update.setDaemon(True)
update.start()

app.mainloop()

print('*** Done')
