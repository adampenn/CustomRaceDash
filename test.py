#!/usr/bin/python3/

import tkinter as tk
from tkinter import ttk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        value_progress = 200
        self.parent.title("Progressbar Thingymawhatsit")
        self.config(bg = '#F0F0F0')
        self.pack(fill = tk.BOTH, expand = 1)
                #create canvas
        canvas = tk.Canvas(self, relief = tk.FLAT, background = "#D2D2D2",
                                            width = 400, height = 5)

        progressbar = ttk.Progressbar(canvas, orient=tk.HORIZONTAL,
                                  length=400, mode="indeterminate",
                                  variable=value_progress,

                                  )
        # The first 2 create window argvs control where the progress bar is placed
        canvas.create_window(1, 1, anchor=tk.NW, window=progressbar)
        canvas.grid()


def main():
    root = tk.Tk()
    root.geometry('500x50+10+50')
    app = Example(root)
    app.mainloop()

if __name__ == '__main__':
    main()
