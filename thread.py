#!/usr/bin/python3

# System modules
import tkinter as tk
#import serial
import time
from tkinter import ttk
from queue import Queue
from threading import Thread

# Set up some global variables
num_fetch_threads = 1
queue = Queue()
#ser = serial.Serial('/dev/ttyACM0',9600)
#s = [0]
 
# This is the thread that reads from the Ardino
def readFromArduino(app, q):
  print("*** Read thread running")
  ser = serial.Serial('/dev/ttyACM0',9600)
  data = [0]
  while True:
    time.sleep(.05)
    data[0] = int (ser.readline())
    #print(s[0])
    q.put(data[0])
   
   
    #RPM = app.scale.get()
    #MPH = 35
    #data = [RPM, MPH]
    #q.put(data)
    #q.task_done()

# Update Gauge Values
def updateGauges(app, q):
  print("*** Update thread running")
  while True:
    time.sleep(.05)
    data = q.get()
    app.RPM["value"] = data[0]
    app.MPH["value"] = 35

# Declare a class for the GUI
class SampleApp(tk.Tk):

  def __init__(self):
    # Init
    tk.Tk.__init__(self)
    self.style = ttk.Style()
    self.style.configure("BW.TLabel", foreground="black")

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

    # Scale for RPM
    self.scale = ttk.Scale(self, from_=0, to=7000, orient="horizontal", length=200)
    self.scale.pack()


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
