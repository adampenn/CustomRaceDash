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
  """This is the worker thread function.
  It processes items in the queue one after
  another.  These daemon threads go into an
  infinite loop, and only exit when
  the main thread ends.
  """
  while True:
    time.sleep(.01)
    #read_serial=ser.readline()
    #s[0] = str(int (ser.readline(),16))
    #print("Reading from Arduino")
    #q.put(s[0])
    #q.put(read_serial)
    q.put(app.scale.get())
    q.task_done()

# Update Gauge Values
def updateGauges(app, q):
  while True:
    time.sleep(.01)
    RPM = q.get()
    app.RPM["value"] = RPM

# Declare a class for the GUI
class SampleApp(tk.Tk):

  def __init__(self):
    tk.Tk.__init__(self)
    self.style = ttk.Style()
    self.style.configure("BW.TLabel", foreground="black", 
                         background="white")
    self.labelRPM = ttk.Label(text="RPM", style="BW.TLabel")
    self.labelRPM.pack()
    self.RPM = ttk.Progressbar(self, orient="horizontal", length=200,
                               mode="determinate", value=0, maximum=7000)
    self.RPM.pack()
    self.scale = ttk.Scale(self, from_=0, to=7000, orient="horizontal")
    self.scale.pack()


#  def get_RPM(self):
#    self.RPM["value"] = self.scale.get()


app = SampleApp()

# Set up some threads
read = Thread(target=readFromArduino, args=(app, queue,))
read.setDaemon(True)
read.start()

update = Thread(target=updateGauges, args=(app, queue,))
update.setDaemon(True)
update.start()

app.mainloop()

print('*** Main thread waiting')
queue.join()
print('*** Done')
