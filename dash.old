#!/usr/bin/python3

# System modules
import tkinter as tk
import serial
import time
from tkinter import ttk
from queue import Queue
from threading import Thread

# Set up some global variables
num_fetch_threads = 1
queue = Queue()
 
# This is the thread that reads from the Ardino
def readFromArduino(app, q):
  print("*** Read thread running")
  ser = serial.Serial('/dev/ttyUSB0',9600)
  data = [0,0,0,0,0,0]
  while True:
    time.sleep(.05)
    q.put((ser.readline()).decode("utf-8"))
    q.task_done()

# Update Gauge Values
def updateGauges(app, q):
  print("*** Update thread running")
  while True:
    time.sleep(.05)
    data = q.get()
    if data[0] == 'T':
      app.Temp["value"] = int(data[1:len(data)])
    if data[0] == 'S':
      app.MPH["value"] = int(data[1:len(data)])
    if data[0] == 'R':
      app.RPM["value"] = int(data[1:len(data)])

# Declare a class for the GUI
class SampleApp(tk.Tk):

  def __init__(self):
    # Init
    tk.Tk.__init__(self)
    self.style = ttk.Style()
    self.style.configure("BW.TLabel", foreground="black")

    # TEMP
    self.labelTemp = ttk.Label(text="Engine Temp C", style="BW.TLabel")
    self.labelTemp.pack()
    self.Temp = ttk.Progressbar(self, orient="horizontal", length=200,
                               mode="determinate", value=0, maximum=150)
    self.Temp.pack()

    # RPM
    self.labelRPM = ttk.Label(text="RPM", style="BW.TLabel")
    self.labelRPM.pack()
    self.RPM = ttk.Progressbar(self, orient="horizontal", length=200,
                               mode="determinate", value=0, maximum=7000)
    self.RPM.pack()

    # MPH
    self.labelMPH = ttk.Label(text="MPH", style="BW.TLabel")
    self.labelMPH.pack()
    self.MPH = ttk.Progressbar(self, orient="horizontal", length=200,
                               mode="determinate", value=0, maximum=140)
    self.MPH.pack()


#  def get_RPM(self):
#    self.RPM["value"] = self.scale.get()

print('*** Main thread running')

app = SampleApp()

# Set up some threads
read = Thread(target=readFromArduino, args=(app, queue,))
read.setDaemon(True)
read.start()

update = Thread(target=updateGauges, args=(app, queue,))
update.setDaemon(True)
update.start()

app.mainloop()

queue.join()
print('*** Done')
