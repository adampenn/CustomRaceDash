import tkinter as tk
from tkinter import ttk

frame = tk.Frame(root)
  frame.grid()
  s = ttk.Style()
  s.theme_use('clam')
  s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
  ttk.Progressbar(frame, style="red.Horizontal.TProgressbar", orient="horizontal", length=600, mode="determinate", maximum=4, value=1).grid(row=1, column=1)
  ttk.Progressbar(frame, orient="horizontal", length=600, mode="determinate", maximum=4, value=1).grid(row=2, column=1) 
  frame.pack()
  root.mainloop()


def main():
    # Init
    tk.Tk.__init__(self)
    style = ttk.Style()
    style.theme_use("calm")
    style.configure("RPMhigh", forground='red', thickness=100)
    style.configure("RPMreg", forground='blue', thickness=100)
    style.configure("BW.TLabel", foreground="black")
    self.geometry('800x480')

    # Set up the different screens
    notebook = ttk.Notebook(self)
    screen1 = ttk.Frame(notebook)
    screen2 = ttk.Frame(notebook)
    notebook.add(screen1, text='Screen 1')
    notebook.add(screen2, text='Screen 2')
    notebook.pack()

    # TEMP
    self.labelTemp = ttk.Label(screen1, text="Engine Temp C", style="BW.TLabel")
    self.labelTemp.pack()
    self.Temp = ttk.Progressbar(screen1, orient="horizontal", length=800,
                               mode="determinate", value=0, maximum=250)
    self.Temp.pack()

    # RPM
    self.labelRPM = ttk.Label(screen1, text="RPM", style="BW.TLabel")
    self.labelRPM.pack()
    self.RPM = ttk.Progressbar(screen1, orient="vertical", length=800,
                               mode="determinate", value=0, maximum=7000)
    self.RPM.pack()

    # MPH
    self.labelMPH = ttk.Label(screen2, text="MPH", style="BW.TLabel")
    self.labelMPH.pack()
    self.MPH = ttk.Progressbar(screen2, orient="horizontal", length=800,
                               mode="determinate", value=0, maximum=120)
    self.MPH.pack()

    # Fuel Level
    self.labelFuelLevel = ttk.Label(screen2, text="Fuel Level", style="BW.TLabel")
    self.labelFuelLevel.pack()
    self.fuelLevel = ttk.Progressbar(screen2, orient="horizontal", length=800,
                               mode="determinate", value=0, maximum=100)
    self.fuelLevel.pack()

    # Intake Temp
    self.labelIntakeTemp = ttk.Label(screen2, text="Intake Temp", style="BW.TLabel")
    self.labelIntakeTemp.pack()
    self.intakeTemp = ttk.Progressbar(screen2, orient="horizontal", length=800,
                               mode="determinate", value=0, maximum=200)
    self.intakeTemp.pack()

main()

