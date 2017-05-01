from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    s = ttk.Style()
    s.theme_use("default")
    s.configure("TProgressbar", thickness=50)
    pb = ttk.Progressbar(root, orient="vertical", style="TProgressbar", value=50, maximum=100, length=800)
    pb.pack()
    slider = ttk.Scale(root, from_=0, to=100, length=800, orient="horizontal")
    slider.pack()
    root.mainloop()

main()
