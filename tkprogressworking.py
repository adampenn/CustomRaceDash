import tkinter as tk
from tkinter import ttk


class SampleApp(tk.Tk):

  def __init__(self):
    tk.Tk.__init__(self)
    self.button = ttk.Button(text="start", command=self.get_RPM)
    self.button.pack()
    self.RPM = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", value=0, maximum=7000)
    self.RPM.pack()
    self.scale = ttk.Scale(self, from_=0, to=7000, orient="horizontal")
    self.scale.pack()

  def get_RPM(self):
    self.RPM["value"] = self.scale.get()


app = SampleApp()
app.mainloop()



