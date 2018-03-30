import Tkinter as tk
import sys

class Canvas(object):
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.size = size

        self.root = tk.Tk()
        self.root.title('Maze Generation Visualizer')
        self.canvas = tk.Canvas(
            self.root, 
            width=width*size, 
            height=height*size
        )
        self.canvas.grid(row=0, column=0)

    def do(self, func):
        self.rect((0, 0), (self.width, self.height))
        self.root.after(50, func)
        self.root.mainloop()

    def line(self, (x1, y1), (x2, y2), color='white'):
        x1 *= self.size
        y1 *= self.size
        x2 *= self.size
        y2 *= self.size
        rect = self.canvas.create_line((x1, y1, x2, y2), fill=color)
        self.canvas.update_idletasks()

    def rect(self, (x1, y1), (x2, y2), color='white'):
        x1 *= self.size
        y1 *= self.size
        x2 *= self.size
        y2 *= self.size
        self.canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        self.canvas.update_idletasks()
